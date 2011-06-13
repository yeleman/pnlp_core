#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from datetime import date

from bolibana_reporting.validator import DataValidator
from bolibana_reporting.errors import MissingData, IncorrectReportData
from bolibana_reporting.models import Entity, EntityType, MonthPeriod
from pnlp_core.models import MalariaReport


class MalariaReportValidator(DataValidator):

    def validate(self):

        no_more_than_text = "%(field2)s (%(f2value)d) can't be more " \
                            "than %(field1)s (%(f1value)d)"
        allcats = ('u5', 'o5', 'pw')
        noo5cat = ('u5', 'pw')
        nopwcat = ('u5', 'o5')

        def test_value_under(fieldref, fieldtest, cats):
            for cat in cats:
                try:
                    dic = {'field2': self.field_name('%s_%s' \
                                                     % (cat, fieldtest)), \
                           'f2value': self.get('%s_%s' % (cat, fieldtest)), \
                           'field1': self.field_name('%s_%s' \
                                                     % (cat, fieldref)), \
                           'f1value': self.get('%s_%s' % (cat, fieldref))}
                    if dic['f1value'] < dic['f2value']:
                        self.errors.add(no_more_than_text % dic, cat)
                except MissingData:
                    # this missing data should have already been reported
                    pass

        # total > malaria cases
        test_value_under('total_consultation_all_causes', 'total_suspected_malaria_cases', allcats)

        # total >  malaria simple
        test_value_under('total_consultation_all_causes', 'total_simple_malaria_cases', nopwcat)

        # total >  malaria severe
        test_value_under('total_consultation_all_causes', 'total_severe_malaria_cases', allcats)

        # suspected > malaria simple
        test_value_under('total_suspected_malaria_cases', 'total_simple_malaria_cases', nopwcat)

        # suspected > malaria severe
        test_value_under('total_suspected_malaria_cases', 'total_severe_malaria_cases', allcats)

        # suspected > malaria tested
        test_value_under('total_suspected_malaria_cases', 'total_tested_malaria_cases', allcats)

        # suspected > malaria confirmed
        test_value_under('total_suspected_malaria_cases', 'total_confirmed_malaria_cases', allcats)

        # suspected > simple + severe
        for cat in nopwcat:
            try:
                dic = {'field2': u"%s + %s" \
                       % (self.field_name('%s_total_simple_malaria_cases' % cat), \
                          self.field_name('%s_total_severe_malaria_cases' % cat)), \
                       'f2value': int(self.get('%s_total_simple_malaria_cases' \
                                               % cat)) \
                                  + int(self.get('%s_total_severe_malaria_cases' \
                                                 % cat)), \
                       'field1': self.field_name('%s_total_suspected_malaria_cases' % cat), \
                       'f1value': self.get('%s_total_suspected_malaria_cases' % cat)}
                if dic['f1value'] < dic['f2value']:
                    self.errors.add(no_more_than_text % dic, cat)
            except MissingData:
                pass

        # tested > confirmed
        test_value_under('total_tested_malaria_cases', \
                         'total_confirmed_malaria_cases', allcats)

        # tested > ACT
        test_value_under('total_tested_malaria_cases', \
                         'total_treated_malaria_cases', allcats)

        # confirmed > act
        test_value_under('total_confirmed_malaria_cases', \
                         'total_treated_malaria_cases', allcats)

        # total inpatient > malaria inpatient
        test_value_under('total_inpatient_all_causes', 'total_malaria_inpatient', allcats)

        # total death > malaria death
        test_value_under('total_death_all_causes', 'total_malaria_death', allcats)

        # PERIOD MONTH
        # range(1, 12)
        # already handled.

        # PERIOD YEAR
        # range(2010, 2020)
        # already handled

        # NO FUTURE
        if self.get('year') >= date.today().year \
           and self.get('month') >= date.today().month:
            self.errors.add(u"La période des données (%s) " \
                            "est dans le futur." % \
                            u"%s %d" % (self.get('month').__str__().zfill(2), \
                                        self.get('year')), 'period')

        # DATE DAY / MONTH / YEAR
        try:
            date(self.get('fillin_year'), \
                 self.get('fillin_month'), self.get('fillin_day'))
        except ValueError:
            self.errors.add(u"The fillin day (%s) is out of range for " \
                            "that month (%s)" \
                            % (self.get('fillin_day').__str__().zfill(2), \
                               self.get('fillin_month').__str__().zfill(2)), \
                               'fillin')

        # REPORTER NAME
        pass

        # ENTITY
        try:
            entity = Entity.objects.get(slug=self.get('hc'), \
                                        type__slug='cscom')
        except Entity.DoesNotExist:
            entity = None
            self.errors.add(u"The entity code (%s) does not match any HC." \
                            % self.get('hc'), 'period')

        # NO DUPLICATE
        period = MonthPeriod.find_create_from(year=self.get('year'), \
                                              month=self.get('month'))
        if entity and MalariaReport.objects.filter(entity=entity, \
                                                   period=period).count() > 0:
            self.errors.add(u"There is already a report for that HC (%s) " \
                            "and that period (%s)" % \
                            (entity.display_full_name(), \
                             period.name()), 'period')
