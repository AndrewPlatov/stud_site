from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import Profile
from .forms import TeacherSignUpForm

def main(request):
    return render(
        request,               # так будет всегда
        'mainpage/main.html',  # путь к шаблону
        # здесь будут данные!
    )

def check(request):
    return render(
        request,               # так будет всегда
        'mainpage/check.html',  # путь к шаблону
        # здесь будут данные!
    )

def home(request):
    return render(request, 'mainpage/home.html')

def summary(request):
    return render(
        request,               # так будет всегда
        'mainpage/summary.html',  # путь к шаблону
        # здесь будут данные!
    )

from . import forms
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            auth.login(request, new_user)
            return redirect('/')
    else:
        user_form = forms.UserRegistrationForm()
    return render(
        request,
        'user/register.html',
        {
            'form': user_form
        })


from django.shortcuts import render

def test1(request):
    return render(request, 'mainpage/test1.html')  

def test2(request):
        return render(request, 'mainpage/test2.html') 
    
def test3(request):
    return render(request, 'mainpage/test3.html') 

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

        # return JsonResponse(
        #     results
        # )
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


def student_cabinet(request):
    return render(request, 'mainpage/student_cabinet.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('name')
        # Обработка загрузки фото
        if 'photo' in request.FILES:
            user.photo = request.FILES['photo']
        user.save()
        return redirect('student_cabinet')
    # На GET запрос - просто перенаправление или форма с текущими данными
    return render(request, 'mainpage/student_cabinet.html')

@login_required
def homework_upload(request):
    if request.method == 'POST':
        # логика обработки файла
        pass
    return render(request, 'mainpage/homework_upload.html')

@login_required
def homework_download(request):
    # логика поиска файла и отдачи пользователю
    pass

@login_required(login_url='login')
def student_cabinet(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        photo = request.FILES.get('photo')

        user.first_name = name
        user.email = email

        if photo:
            if hasattr(user, 'profile'):
                user.profile.photo = photo
                user.profile.save()
            else:

                user.photo = photo

        user.save()
        messages.success(request, 'Профиль успешно обновлен.')
        return redirect('student_cabinet')

    return render(request, 'mainpage/student_cabinet.html', {'user': user})

def student_cabinet(request):
    return render(request, 'mainpage/student_cabinet.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('student_cabinet')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def update_profile(request):
    user = request.user

    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=user)

    if request.method == 'POST':
        profile.name = request.POST.get('name', profile.name)
        profile.lastname = request.POST.get('lastname', profile.lastname)

        email = request.POST.get('email', user.email)
        if email and email != user.email:
            user.email = email
            user.save()

        if 'photo' in request.FILES:
            profile.photo = request.FILES['photo']

        profile.save()
        messages.success(request, 'Профиль успешно обновлён.')

    return render(request, 'mainpage/student_cabinet.html', {
        'profile': profile,
        'user': user,
    })

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Если есть кастомное поле для роли
            # user.is_teacher = True
            user.save()
            login(request, user)  # сразу логиним пользователя

            # Можно сохранить данные профиля учителя при необходимости

            return redirect('teacher_profile')
    else:
        form = TeacherSignUpForm()
    return render(request, 'mainpage/teacher_register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def teacher_profile(request):
    # можно добавить логику, если нужно отобразить данные учителя
    return render(request, 'mainpage/teacher_profile.html', {'user': request.user})

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Возможно, проверить, что пользователь - учитель, если есть такая логика
            login(request, user)
            return redirect('teacher_profile')  # или куда нужно после входа
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
    
    return render(request, 'mainpage/teacher_login.html')

def teacher_profile(request):
    return render(request, 'mainpage/teacher_profile.html')

# ------------------------------------------------------------------------------- #
# @login_required
# def teacher_profile(request):
#     user = request.user

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name', '').strip()
#         last_name = request.POST.get('last_name', '').strip()
#         email = request.POST.get('email', '').strip()
#         username = request.POST.get('username', '').strip()

#         # Простейшая валидация (можно расширить)
#         if not first_name or not last_name or not email or not username:
#             messages.error(request, 'Пожалуйста, заполните все поля.')
#         else:
#             user.first_name = first_name
#             user.last_name = last_name
#             user.email = email
#             user.username = username
#             user.save()
#             messages.success(request, 'Данные успешно обновлены.')
#             return redirect('teacher_profile')

#     return render(request, 'mainpage/teacher_profile.html')

