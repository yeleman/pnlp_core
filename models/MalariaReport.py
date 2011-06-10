#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from django.db import models
from bolibana_reporting.models import *
from pnlp_core.models import (MalariaUnderFiveReport, MalariaOverFiveReport, \
                              MalariaPregnantWomenReport, \
                              MalariaStockOutsReport)


class MalariaReport(Report):

    class Meta:
        app_label = 'pnlp_core'

    under_five_report = models.OneToOneField('MalariaUnderFiveReport', \
                                             null=False, blank=True)
    over_five_report = models.OneToOneField('MalariaOverFiveReport', \
                                            null=False, blank=True)
    pregnant_women_report = models.OneToOneField('MalariaPregnantWomenReport', \
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
                     pregnant_women_report=pw, stock_outs=so, \
                     type=cls.TYPE_SOURCE)
        for arg, value in kwargs.items():
            try:
                setattr(report, arg, value)
            except AttributeError:
                pass
        report.save()

        for part in parts:
            print "doing part %s" % part
            eval(part).report = report
            eval(part).save()
        print "done parting"
        return report

    def add_underfive_data(self, \
                           total_consultation_all_causes=None, \
                           total_suspected_malaria_cases=None, \
                           total_simple_malaria_cases=None, \
                           total_severe_malaria_cases=None, \
                           total_tested_malaria_cases=None, \
                           total_confirmed_malaria_cases=None, \
                           total_treated_malaria_cases=None, \
                           total_inpatient_all_causes=None, \
                           total_malaria_inpatient=None, \
                           total_death_all_causes=None, \
                           total_malaria_death=None, \
                           total_distributed_bednets=None):
        for field in self.under_five_report._meta.fields:
            try:
                field_value = kwargs[field]
            except AttributeError:
                field_value = eval(field)
            except:
                field = None
                field_value = None

            try:
                if field:
                    setattr(self.report.under_five_report, field, field_value)
            except AttributeError:
                pass
        self.under_five_report.save()

reversion.register(MalariaReport)

