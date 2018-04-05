from django.db import models


# Criaremos uma classe nomeada: "Category", herdando da classe Model
class Category(models.Model):
	name = models.CharField(max_length=255)

