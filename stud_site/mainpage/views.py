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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика формы регистрации 

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика первого варианта системы тестирования

from django.shortcuts import render

def test1(request):
    return render(request, 'mainpage/test1.html')  

def test2(request):
        return render(request, 'mainpage/test2.html') 
    
def test3(request):
    return render(request, 'mainpage/test3.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика обработки первого варианта системы тестирования 

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

def student_cabinet(request):
    return render(request, 'mainpage/student_cabinet.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps

def teacher_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('teacher_login'))  # заменить на ваше имя url логина

        # Проверяем атрибут или группу, которая подтверждает, что пользователь - учитель
        if not getattr(user, 'is_teacher', False):
            return redirect(reverse('not_authorized'))  # или другая страница

        return view_func(request, *args, **kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

@teacher_login_required
def homework_upload(request):
    if request.method == 'POST':
        # логика обработки файла
        pass
    return render(request, 'mainpage/homework_upload.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

@teacher_login_required
def homework_download(request):
    # логика поиска файла и отдачи пользователю
    pass

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

def student_cabinet(request):
    return render(request, 'mainpage/student_cabinet.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

@teacher_login_required
def teacher_profile(request):
    # можно добавить логику, если нужно отобразить данные учителя
    return render(request, 'mainpage/teacher_profile.html', {'user': request.user})

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

def teacher_profile(request):
    return render(request, 'mainpage/teacher_profile.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# mainpage/views.py

from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, AnswerFormSet

def create_test(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question = question_form.save()
            formset = AnswerFormSet(request.POST, instance=question)
            if formset.is_valid():
                formset.save()
                return redirect('test_list')
            else:
                # если formset невалиден, показываем ошибки
                question.delete()  # очищаем вопрос, если ответы невалидны
        else:
            formset = AnswerFormSet(request.POST)
    else:
        question_form = QuestionForm()
        formset = AnswerFormSet()

    return render(request, 'mainpage/create_test.html', {
        'question_form': question_form,
        'formset': formset
    })

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# mainpage/views.py

from django.shortcuts import render
from .models import Question

def test_list(request):
    questions = Question.objects.prefetch_related('answers').all()
    return render(request, 'mainpage/test_list.html', {'questions': questions})

from django.shortcuts import render, redirect, get_object_or_404
from mainpage.forms import TestCreateForm  # импорт формы с учетом изменений

def merge_test(request):
    if request.method == 'POST':
        form = TestCreateForm(request.POST)
        if form.is_valid():
            test = form.save()
            return redirect('test_list')
    else:
        form = TestCreateForm()
    return render(request, 'mainpage/merge_test.html', {'form': form})
    
from mainpage.models import Test

def delete_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == 'POST':
        test.delete()
        return redirect('test_list')
    return render(request, 'mainpage/confirm_delete.html', {'test': test})


def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    result = None

    if request.method == 'POST':
        user_answers = {}
        for question in questions:
            ans_id = request.POST.get(f'question_{question.id}')
            if ans_id:
                user_answers[question.id] = int(ans_id)

        total_questions = questions.count()
        correct_count = 0

        for question in questions:
            correct_answers = question.answer_set.filter(is_correct=True).values_list('id', flat=True)
            selected = user_answers.get(question.id)
            if selected in correct_answers:
                correct_count += 1

        result = {
            'total': total_questions,
            'correct': correct_count,
            'percent': round(correct_count / total_questions * 100, 2) if total_questions else 0,
        }

    return render(request, 'mainpage/take_test.html', {
        'test': test,
        'questions': questions,
        'result': result,
    })

from django.shortcuts import render
from mainpage.models import Test, Question

def main(request):
    test = Test.objects.last()
    questions = test.questions.all() if test else []
    result = None

    if request.method == 'POST' and test:
        # Собираем ответы пользователя из POST
        user_answers = {}  # {question_id: answer_id}
        for question in questions:
            ans_id = request.POST.get(f'question_{question.id}')
            if ans_id:
                user_answers[question.id] = int(ans_id)

        # Подсчет правильных ответов
        total_questions = questions.count()
        correct_count = 0

        for question in questions:
            correct_answers = question.answer_set.filter(is_correct=True).values_list('id', flat=True)
            selected = user_answers.get(question.id)

            # Для теста с одним правильным вариантом:
            if selected in correct_answers:
                correct_count += 1

        result = {
            'total': total_questions,
            'correct': correct_count,
            'percent': round(correct_count / total_questions * 100, 2) if total_questions > 0 else 0,
        }

    return render(request, 'mainpage/main.html', {
        'test': test,
        'questions': questions,
        'result': result,
    })
    
from mainpage.models import Test

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'mainpage/test_list.html', {'tests': tests})


def take_test(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = test.questions.prefetch_related('answers').all()  # assuming related_name='questions' и 'answers'

    return render(request, 'mainpage/take_test.html', {
        'test': test,
        'questions': questions,
    })

def edit_test(request):
    questions = Question.objects.all()  # либо фильтровать по нужному тесту
    return render(request, 'mainpage/edit_test.html', {'questions': questions})

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика редактирования, удаления и создания вопроса для теста

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer 
from .forms import QuestionForm, AnswerFormSet

def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, instance=question)
        formset = AnswerFormSet(request.POST, instance=question)
        if question_form.is_valid() and formset.is_valid():
            question_form.save()
            formset.save()
            return redirect('test_list')  # перенаправить на список тестов или нужную страницу
    else:
        question_form = QuestionForm(instance=question)
        formset = AnswerFormSet(instance=question)

    return render(request, 'mainpage/create_test.html', {
        'question_form': question_form,
        'formset': formset,
        'is_edit': True,  # если хотите показать заголовок редактирования в шаблоне
    })

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        return redirect('edit_test')  # перенаправить обратно на список
    return render(request, 'mainpage/question_confirm_delete.html', {'question': question})

def question_create(request):
    # Логика создания вопроса
    return render(request, 'mainpage/question_create.html')

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

from django.shortcuts import render
from .models import Test

def student_test_list(request):
    # Получаем список тестов (возможно, фильтруете по условиям)
    tests = Test.objects.all()

    context = {
        'tests': tests,
    }
    return render(request, 'mainpage/student_test_list.html', context)
    

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserEditForm, ProfileEditForm

@login_required(login_url='teacher_login')
def edit_teacher_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('teacher_profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'mainpage/edit_teacher_profile.html', context)
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

# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика обработки тестов 

from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Question, Answer

def get_grade(percent):
    if percent >= 90:
        return 5
    elif percent >= 75:
        return 4
    elif percent >= 50:
        return 3
    else:
        return 2

def take_test(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()

    if request.method == 'POST':
        results = []
        total_questions = questions.count()
        correct_count = 0
        wrong_count = 0

        for question in questions:
            selected_answer_ids = request.POST.getlist(f'question_{question.id}')
            selected_answer_ids_set = set(int(id) for id in selected_answer_ids)

            correct_answers = question.answers.filter(is_correct=True)
            correct_answer_ids = set(correct_answers.values_list('id', flat=True))

            # Считаем верно только если выбран набор ответов полностью совпадает с правильным
            if selected_answer_ids_set == correct_answer_ids:
                correct = True
                correct_count += 1
            else:
                correct = False
                wrong_count += 1

            selected_answers_text = [answer.text for answer in question.answers.filter(id__in=selected_answer_ids_set)]
            correct_answers_text = [answer.text for answer in correct_answers]

            results.append({
                'question': question.text,
                'selected_answers': selected_answers_text,
                'correct_answers': correct_answers_text,
                'is_correct': correct,
            })

        percent = (correct_count / total_questions) * 100 if total_questions else 0
        grade = get_grade(percent)
        
        return render(request, 'mainpage/test_result.html', {
            'test': test,
            'results': results,
            'correct_count': correct_count,
            'wrong_count': wrong_count,
            'percent': percent,
            'grade': grade,
            'total': total_questions,
        })
    else:
        # GET — вывод формы
        return render(request, 'mainpage/take_test.html', {
            'test': test,
            'questions': questions,
        })
        
# ----------------------------------------------------------------------------------------------------------------------------------------------- #

# логика вывода результата тестирования

def test_result(request):
    user_answers = request.session.get('user_answers')
    test_id = request.session.get('test_id')

    if not user_answers or not test_id:
        # Если нет данных — редирект на список тестов или на главную
        return redirect('test_list')

    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()

    results = []
    total_questions = questions.count()
    correct_count = 0
    wrong_count = 0

    for question in questions:
        selected_answer_ids = user_answers.get(str(question.id), [])
        selected_answer_ids_set = set(int(id) for id in selected_answer_ids)

        correct_answers = question.answers.filter(is_correct=True)
        correct_answer_ids = set(correct_answers.values_list('id', flat=True))

        if selected_answer_ids_set == correct_answer_ids:
            correct = True
            correct_count += 1
        else:
            correct = False
            wrong_count += 1

        selected_answers_text = [answer.text for answer in question.answers.filter(id__in=selected_answer_ids_set)]
        correct_answers_text = [answer.text for answer in correct_answers]

        results.append({
            'question': question.text,
            'selected_answers': selected_answers_text,
            'correct_answers': correct_answers_text,
            'is_correct': correct,
        })

    percent = (correct_count / total_questions) * 100 if total_questions else 0
    grade = get_grade(percent)

    # Можно очистить сессию, если нужно
    # del request.session['user_answers']
    # del request.session['test_id']

    return render(request, 'maipage/test_result.html', {
        'test': test,
        'results': results,
        'correct_count': correct_count,
        'wrong_count': wrong_count,
        'percent': percent,
        'grade': grade,
        'total': total_questions,
    })

# ----------------------------------------------------------------------------------------------------------------------------------------------- #