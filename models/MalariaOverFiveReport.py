#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from bolibana_reporting.models import *


class MalariaOverFiveReport(ReportPart):

    class Meta:
        app_label = 'pnlp_core'

    # OVER FIVE
    total_consultation_all_causes = models.PositiveIntegerField(null=True, \
                                                                blank=True)
    total_suspected_malaria_cases = models.PositiveIntegerField(null=True, \
                                                                blank=True)
    total_simple_malaria_cases = models.PositiveIntegerField(null=True, \
                                                             blank=True)
    total_severe_malaria_cases = models.PositiveIntegerField(null=True, \
                                                             blank=True)
    total_tested_malaria_cases = models.PositiveIntegerField(null=True, \
                                                             blank=True)
    total_confirmed_malaria_cases = models.PositiveIntegerField(null=True, \
                                                                blank=True)
    total_treated_malaria_cases = models.PositiveIntegerField(null=True, \
                                                              blank=True)

    total_inpatient_all_causes = models.PositiveIntegerField(null=True, \
                                                             blank=True)
    total_malaria_inpatient = models.PositiveIntegerField(null=True, \
                                                          blank=True)

    total_death_all_causes = models.PositiveIntegerField(null=True, \
                                                         blank=True)
    total_malaria_death = models.PositiveIntegerField(null=True, \
                                                      blank=True)
