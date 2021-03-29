from django.contrib import admin

# Register your models here.
from . import models
# 每个表都在本地进行注册
admin.site.register(models.Env)