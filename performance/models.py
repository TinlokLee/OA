from django.db import models
from django.utils.encoding import smart_str
from django_OA import settings
from user.models import Department


class QestionNaire(models.Model):
    ''' 问卷调查 '''
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    type = models.CharField(max_length=20, chioce=(
        ("downtoup", "下对上"),
        ("updtodown", "上对下"),
        ("uptoup", "平级")
    ), verbose_name="类型", default="uptoup")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="所属部门")
    question = models.ManyToManyField("Question", related_name="questionnaire_level_question", verbose_name="问题")

    def __str__(self):
        return smart_str(self.department.name + "的" + self.type + "的问卷")

    class Meta:
        verbose_name = "问卷"
        verbose_name_plural = verbose_name
        ordering = ["-created_at"]


class Question(models.Model):
    question_type = models.CharField(max_length=20, verbose_name="评价指标", null=False)
    question_content = models.CharField(max_length=200, verbose_name="评价要素", null=False)
    full_score = models.IntegerField(verbose_name="标准分值", null=False)
    order_in_list = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return smart_str(self.question_type + " " + self.question_content)


class AssessmentRelationship(models.Model):
    ''' 评估关系 '''
    judge = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="judge"
                              on_delete=models.CASCADE, verbose_name="评分人")
    palyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="player"
                              on_delete=models.CASCADE, verbose_name="受评人")
    questionnaire = models.ForeignKey("Qusetionnarie", on_delete=models.CASCADE, verbose_name="对应问卷")
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")
    modified_at = models.DateTimeField(auto_now=True, editable=False, verbose_name="提交时间")

    class Meta:
        verbose_name = "考勤关系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return smart_str(self.judge.first_name + "对" + self.player.first_name + "评价")


class AnswerSheet(models.Model):
    answer_sheet_base = models.ForeignKey("Assessment")



class Answer(models.Model):

