from django.db import models

# Create your models here.
class Memo(models.Model):
    content = models.CharField(max_length=1000, blank=True, null=True) # 메모 컨텐트 정의