#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from bolibana_reporting.models import *


class MalariaStockOutsReport(ReportPart):

    class Meta:
        app_label = 'pnlp_core'

    YES = 1
    NO = 0
    YESNO = ((YES, u"Yes"), (NO, u"No"))

    # STOCK OUTS
    stockout_act_children = models.CharField(max_length=1, choices=YESNO, \
                                             null=True, blank=True)
    stockout_act_youth = models.CharField(max_length=1, choices=YESNO, \
                                          null=True, blank=True)
    stockout_act_adult = models.CharField(max_length=1, choices=YESNO, \
                                          null=True, blank=True)

    stockout_arthemeter = models.CharField(max_length=1, choices=YESNO, \
                                           null=True, blank=True)
    stockout_quinine = models.CharField(max_length=1, choices=YESNO, \
                                        null=True, blank=True)
    stockout_serum = models.CharField(max_length=1, choices=YESNO, \
                                      null=True, blank=True)

    stockout_bednet = models.CharField(max_length=1, choices=YESNO, \
                                       null=True, blank=True)
    stockout_rdt = models.CharField(max_length=1, choices=YESNO, \
                                    null=True, blank=True)
    stockout_sp = models.CharField(max_length=1, choices=YESNO, \
                                   null=True, blank=True)
