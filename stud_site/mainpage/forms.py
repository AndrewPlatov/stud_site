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
    

# mainpage/forms.py

from django import forms
from .models import Question, Answer
from django.forms import inlineformset_factory

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'big-question-field',
                'rows': 6,
                'placeholder': 'Введите текст вопроса здесь...'
            }),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'is_correct']

AnswerFormSet = inlineformset_factory(
    Question,
    Answer,
    form=AnswerForm,
    extra=4,  # по умолчанию 4 варианта ответов
    can_delete=False,
    min_num=1,
    validate_min=True
)


from django import forms
from mainpage.models import Question, Answer, Test

class TestCreateForm(forms.ModelForm):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Test
        fields = ['title', 'questions']