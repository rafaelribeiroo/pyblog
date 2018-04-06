from django.db import models


# Criaremos uma classe nomeada: "Category", herdando da classe Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    status_choices = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default='Draft',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name
