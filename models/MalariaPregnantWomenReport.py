#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from bolibana_reporting.models import *


class MalariaPregnantWomenReport(ReportPart):

    class Meta:
        app_label = 'pnlp_core'

    # PREGNANT WOMEN
    total_consultation_all_causes = models.PositiveIntegerField(null=True, \
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

    total_distributed_bednets = models.PositiveIntegerField(null=True, \
                                                            blank=True)

    # ANTENATAL CARE
    total_anc1 = models.PositiveIntegerField(null=True, blank=True)
    total_sp1 = models.PositiveIntegerField(null=True, blank=True)
    total_sp2 = models.PositiveIntegerField(null=True, blank=True)
