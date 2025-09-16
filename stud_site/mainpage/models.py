from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('multiple-choice', 'Множественный выбор'),
        ('text-input', 'Текстовый ввод'),
    ]
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)
    answers = models.JSONField(blank=True, null=True)  # Для вариантов ответов
    correct_answers = models.JSONField()  # Для правильных ответов

    def __str__(self):
        return self.question_text

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
