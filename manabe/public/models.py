from django.db import models


# 将以后每个表都可以用到的公共字段进行提取
class CommonInfo(models.Model):
    name = models.CharField(max_length=100,
                            unique=True,
                            verbose_name="名称")
    description = models.CharField(max_length=100,
                                   blank=True,
                                   null=True,
                                   verbose_name="描述")
    change_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    # 表示该类无法创建任何数据表,但其被继承之后该类中的字段会被添加到子类中
    class Meta:
        abstract = True
        ordering = ('-change_date',)

