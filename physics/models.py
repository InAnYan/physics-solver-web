from django.db import models


class Example(models.Model):
    text = models.TextField()


class ProblemIssueReport(models.Model):
    is_solved = models.BooleanField()
    problem_text = models.TextField()
    comment = models.TextField()
    date = models.DateTimeField()


class ImprovementReport(models.Model):
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
