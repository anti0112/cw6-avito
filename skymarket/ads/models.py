from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

class Ad(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField('ad_image', null=True)
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title
        

class Comment(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.title
    