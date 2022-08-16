from django.db import models


class Category(models.Model):
    '''Модель категорий'''
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    mini_text = models.TextField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    text = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


    def __str__(self):
        return self.text