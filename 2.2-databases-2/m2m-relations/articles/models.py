from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length = 25, unique = True, verbose_name = 'Тег')
    article = models.ManyToManyField(Article, related_name ='tag', through = 'Scope')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
    
class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name ='scopes', verbose_name = 'Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name ='scopes', verbose_name='Тег')
    is_main = models.BooleanField(default=False, verbose_name='Главный тег')

    class Meta:
        verbose_name = 'Тег статьи'
        verbose_name_plural = 'Теги статьи'

    def __str__(self):
        return f' {self.article} {self.tag}'