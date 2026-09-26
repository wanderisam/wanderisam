from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField (max_length=200)
    slug =models.SlugField(unique=True)
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField( max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/',blank=True ,null=True)
    available = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now_add=True)







