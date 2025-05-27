from django.shortcuts import render

def main(request):
    return render(
        request, 
        'mainpage/main.html'
    )
    
from django.shortcuts import render

def test1(request):
    return render(request, 'mainpage/test1.html')   

from django.shortcuts import render, redirect
from .models import Question

def quiz(request):
    questions = list(Question.objects.all())
    total_questions = len(questions)

    if 'current_index' not in request.session:
        request.session['current_index'] = 0
        request.session['score'] = 0
        request.session['results'] = []

    current_index = request.session['current_index']
    score = request.session['score']
    results = request.session['results']

    if current_index >= total_questions:
        # Тест завершен, показываем результаты
        grade = calculate_grade(score, total_questions)
        context = {
            'score': score,
            'total': total_questions,
            'grade': grade,
            'results': results,
        }
        # Очистка сессии для нового теста при повторе
        del request.session['current_index']
        del request.session['score']
        del request.session['results']
        return render(request, 'quiz/result.html', context)

    question = questions[current_index]

    if request.method == 'POST':
        user_answers = None
        is_correct = False

        if question.question_type == 'text-input':
            user_input = request.POST.get('user_answer', '').strip()
            correct_answers = question.correct_answers
            is_correct = any(user_input.lower() == ans.lower() for ans in correct_answers)
            user_answers = [user_input]
        else:
            user_answers = request.POST.getlist('answers')
            correct_answers_set = set(ans.lower() for ans in question.correct_answers)
            user_answers_set = set(ans.lower() for ans in user_answers)
            is_correct = correct_answers_set == user_answers_set

        # Обновляем результаты и счетчик
        results.append({
            'question': question.question_text,
            'user_answers': user_answers,
            'correct_answers': question.correct_answers,
            'is_correct': is_correct,
        })

        if is_correct:
            request.session['score'] += 1

        # Переход к следующему вопросу
        request.session['current_index'] += 1
        request.session['results'] = results

        return redirect('quiz')

    context = {
        'question': question,
    }
    return render(request, 'quiz/question.html', context)

def calculate_grade(score, total):
    percentage = score / total
    if percentage == 1:
        return 5
    elif percentage >= 0.8:
        return 4
    elif percentage >= 0.6:
        return 3
    elif percentage >= 0.4:
        return 2
    else:
        return 1