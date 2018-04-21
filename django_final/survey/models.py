# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class SurveyQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    respondent = models.CharField(max_length=100)
	
    def __str__(self):
	    return self.question_text

@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	
    def __str__(self):
	return self.choice_text
