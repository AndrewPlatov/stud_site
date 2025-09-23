# from django import forms
# from django.contrib.auth.models import User

# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_password_confirm(self):
#         password = self.cleaned_data.get('password')
#         password_confirm = self.cleaned_data.get('password_confirm')
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError("Пароли не совпадают")
#         return password_confirm

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя')
    email = forms.EmailField(label='Электронная почта')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user
    
class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    

# forms.py
from django import forms
from django.forms.models import inlineformset_factory
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['test', 'text', 'question_type']

AnswerFormSet = inlineformset_factory(
    Question,
    Answer,
    fields=['text', 'is_correct'],
    extra=3,  # количество пустых форм для ответов по умолчанию
    can_delete=True
)


# forms.py
from django import forms
from .models import Question, Answer

class TestTakeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')  # queryset с вопросами теста
        super().__init__(*args, **kwargs)

        for question in questions:
            answers = question.answers.all()
            choices = [(answer.id, answer.text) for answer in answers]

            if question.question_type == Question.SINGLE_CHOICE:
                self.fields[f'question_{question.id}'] = forms.ChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.RadioSelect,
                    required=True
                )
            else:  # MULTIPLE_CHOICE
                self.fields[f'question_{question.id}'] = forms.MultipleChoiceField(
                    label=question.text,
                    choices=choices,
                    widget=forms.CheckboxSelectMultiple,
                    required=True
                )