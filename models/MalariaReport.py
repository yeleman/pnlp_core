#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from bolibana_reporting.models import *


class MalariaReport(Report):

    class Meta:
        app_label = 'pnlp_core'

    under_five_report = models.OneToOneField('MalariaUnderFiveReport', \
                                             null=False, blank=True)
    over_five_report = models.OneToOneField('MalariaOverFiveReport', \
                                            null=False, blank=True)
    pregnan_women_report = models.OneToOneField('MalariaPregnantWomenReport', \
                                                null=False, blank=True)
    stock_outs = models.OneToOneField('MalariaStockOutsReport', \
                                      null=False, blank=True)

    @classmethod
    def create(cls, period, entity, author, *args, **kwargs):

        parts = ['u5', 'o5', 'pw', 'so']
        u5 = MalariaUnderFiveReport()
        o5 = MalariaOverFiveReport()
        pw = MalariaPregnantWomenReport()
        so = MalariaStockOutsReport()
        for part in parts:
            eval(part).save()

        report = cls(period=period, entity=entity, created_by=author, \
                     modified_by=author, _status=cls.STATUS_UNSAVED, \
                     under_five_report=u5, over_five_report=o5, \
                     pregnan_women_report=pw, stock_outs=so)
        for arg, value in kwargs.items():
            try:
                setattr(report, arg, value)
            except AttributeError:
                pass
        report.save()

        for part in parts:
            eval(part).report = report
            eval(part).save()

        return report
