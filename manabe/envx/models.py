from django.db import models
from public.models import CommonInfo
# create model
class Env(CommonInfo):
    eid = models.IntegerField(unique=True,verbose_name="环境序号")

