from django.db import models

# Create your models here.
class ShopTipModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    register_date = models.DateField(auto_now=True)

    def __str__(self) -> str:   # !!!! pythonの仕組みを確認
        return self.title
    
class RecordedTask(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    register_date = models.DateField(auto_now=True)

    def __str__(self) -> str:   # !!!! pythonの仕組みを確認
        return self.title
    