from django.db import models

# Create your models here.

# 投票应用中将创建两个模型: Question和 Choice

# Question两个字段 question_text和publish_date
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

# Choice 两个字段 choice_text 和 votes ,每个Choice和Question都有联系

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# toString方法 python 是__str__(self) 方法

	
