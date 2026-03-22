from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description=models.CharField(max_length=200)
    stock=models.PositiveIntegerField(default=0, verbose_name='Остаток')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering=['-created_at','price']
