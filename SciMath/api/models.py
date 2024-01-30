from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

Phy = "Physics"
Chem = "Chemistry"
Bioz = "Biology"
Math = "Mathematics"
SUBJECTS = (
        (Phy, "Physics"),
        (Chem, "Chemistry"),
        (Bioz, "Biology"),
        (Math, "Mathematics"),
    )

class category(models.Model):
   
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]

    category = models.ForeignKey(category, default=1, on_delete=models.PROTECT)
    title = models.CharField(
        max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title")
    )
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Questions(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]


    SCALE = (
        (0, _("Form One")),
        (1, _("Form Two")),
        (2, _("Form Three")),
        (3, _("Form Four")),
        (4, _("Form Five")),
        (5, _("Form Six")),
    )

    TYPE = (
       ( 0,_("Multiple choice")),
    )

    quiz = models.ForeignKey(
        Quizzes, related_name="question", on_delete=models.PROTECT
    )
    topic = models.ForeignKey(
        category, on_delete=models.PROTECT
    )
    subject_name= models.CharField(max_length=255, choices=SUBJECTS, default=Phy, null=False)
    

    Level = models.IntegerField(
        choices=SCALE, default=0, verbose_name=_("Level")
    )
    title = models.CharField(max_length=255, verbose_name=_("Question Title"))
    
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Created")
    )
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answers(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]

    question = models.ForeignKey(
        Questions, related_name="answer", on_delete=models.PROTECT
    )
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.answer_text