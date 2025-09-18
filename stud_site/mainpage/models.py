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


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)

    def __str__(self):
        return f'Профиль {self.user.username}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)