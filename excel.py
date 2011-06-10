#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from datetime import date

from bolibana_reporting.excel import (ExcelForm, ExcelFormField, \
                                      ExcelTypeConverter)
from bolibana_reporting.models import Period, MonthPeriod, Entity
from pnlp_core.models import MalariaReport


class MalariaExcelForm(ExcelForm):

    YN_MAP = {'oui': u"Y", 'non': u"N", '': u"U", None:u"U"}
    MONTH_MAP = range(1, 13)
    YEAR_MAP = range(2011, 2021)
    DAY_MAP = range(1, 32)

    _mapping = {'0.3': {
    'region': ExcelFormField('B2', unicode, u"Région", attr='region'),
    'district': ExcelFormField('B3', unicode, u"District sanitaire", \
                                attr='district'),
    'hc': ExcelFormField('B4', unicode, u"Établissement sanitaire", \
                          attr='health_center'),
    'month': ExcelFormField('D3', ExcelTypeConverter.NormalizedIntChoiceList, \
                            u"Mois", cast_args=MONTH_MAP, attr='month'),
    'year': ExcelFormField('G3', ExcelTypeConverter.NormalizedIntChoiceList, \
                           u"Année", cast_args=YEAR_MAP, attr='year'),

    'total_consultation_u5': ExcelFormField('C7', int, \
                    u"Total consultation, toutes causes confondues", \
                    attr='total_consult_u5'),
    'total_consultation_5p': ExcelFormField('E7', int, \
                u"Total consultation, toutes causes confondues", \
                attr='total_consult_5p'),
    'total_consultation_fe': ExcelFormField('G7', int, \
                                        u"Total consultation, toutes causes " \
                                        "confondues", \
                                         attr='total_consult_fe'),

    'total_malaria_u5': ExcelFormField('C8', int, \
                       u"Nbre de Cas de paludisme (Tous suspectés)", \
                       attr='total_malaria_u5'),
    'total_malaria_5p': ExcelFormField('E8', int, \
                   u"Nbre de Cas de paludisme (Tous suspectés)", \
                   attr='total_malaria_5p'),
    'total_malaria_fe': ExcelFormField('G8', int, \
             u"Nbre de Cas de paludisme (Tous suspectés)", \
             attr='total_malaria_fe'),

    'total_malaria_simple_u5': ExcelFormField('C9', int, \
                                 u"Nbre de Cas de paludisme Simple", \
                                 attr='total_malaria_simple_u5'),
    'total_malaria_simple_5p': ExcelFormField('E9', int, \
                             u"Nbre de Cas de paludisme Simple", \
                             attr='total_malaria_simple_5p'),

    'total_malaria_severe_u5': ExcelFormField('C10', int, \
                                  u"Nbre de Cas de paludisme Grave", \
                                  attr='total_malaria_severe_u5'),
    'total_malaria_severe_5p': ExcelFormField('E10', int, \
                              u"Nbre de Cas de paludisme Grave", \
                              attr='total_malaria_severe_5p'),
    'total_malaria_severe_fe': ExcelFormField('G10', int, \
                        u"Nbre de Cas de paludisme Grave", \
                        attr='total_malaria_severe_fe'),

    'total_malaria_tested_u5': ExcelFormField('C11', int, \
                          u"Cas de paludisme testés (GE et/ou TDR)", \
                          attr='total_malaria_tested_u5'),
    'total_malaria_tested_5p': ExcelFormField('E11', int, \
                      u"Cas de paludisme testés (GE et/ou TDR)", \
                      attr='total_malaria_tested_5p'),
    'total_malaria_tested_fe': ExcelFormField('G11', int, \
                                         u"Cas de paludisme testés " \
                                         "(GE et/ou TDR)", \
                                         attr='total_malaria_tested_fe'),

    'total_malaria_confirmed_u5': ExcelFormField('C12', int, \
                       u"Cas de paludisme confirmés (GE et/ou TDR)", \
                       attr='total_malaria_confirmed_u5'),
    'total_malaria_confirmed_5p': ExcelFormField('E12', int, \
                   u"Cas de paludisme confirmés (GE et/ou TDR)", \
                   attr='total_malaria_confirmed_5p'),
    'total_malaria_confirmed_fe': ExcelFormField('G12', int, \
                                         u"Cas de paludisme confirmés " \
                                         "(GE et/ou TDR)", \
                                         attr='total_malaria_confirmed_fe'),

    'total_malaria_acttreated_u5': ExcelFormField('C13', int, \
                                    u"Nbre de Cas traités avec CTA", \
                                    attr='total_malaria_acttreated_u5'),
    'total_malaria_acttreated_5p': ExcelFormField('E13', int, \
                                u"Nbre de Cas traités avec CTA", \
                                attr='total_malaria_acttreated_5p'),
    'total_malaria_acttreated_fe': ExcelFormField('G13', int, \
                          u"Nbre de Cas traités avec CTA", \
                          attr='total_malaria_acttreated_fe'),

    'total_malaria_inpatient_u5': ExcelFormField('C18', int, \
                                    u"Total Hospitalisés Paludisme", \
                                    attr='total_malaria_inpatient_u5'),
    'total_malaria_inpatient_5p': ExcelFormField('E18', int, \
                                u"Total Hospitalisés Paludisme", \
                                attr='total_malaria_inpatient_5p'),
    'total_malaria_inpatient_fe': ExcelFormField('G18', int, \
                          u"Total Hospitalisés Paludisme", \
                          attr='total_malaria_inpatient_fe'),

    'total_inpatient_u5': ExcelFormField('C17', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_u5'),
    'total_inpatient_5p': ExcelFormField('E17', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_5p'),
    'total_inpatient_fe': ExcelFormField('G17', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_fe'),

    'total_malaria_death_u5': ExcelFormField('C23', int, \
                                     u"Cas de décès pour paludisme", \
                                     attr='total_malaria_death_u5'),
    'total_malaria_death_5p': ExcelFormField('E23', int, \
                                 u"Cas de décès pour paludisme", \
                                 attr='total_malaria_death_5p'),
    'total_malaria_death_fe': ExcelFormField('G23', int, \
                           u"Cas de décès pour paludisme", \
                           attr='total_malaria_death_fe'),

    'total_death_u5': ExcelFormField('C22', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_u5'),
    'total_death_5p': ExcelFormField('E22', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_5p'),
    'total_death_fe': ExcelFormField('G22', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_fe'),

    'total_bednets_u5': ExcelFormField('C27', int, \
                                      u"Nombre de moustiquaires distribuées " \
                                      u"(< 5ans)", attr='total_bednets_u5'),
    'total_bednets_fe': ExcelFormField('E27', int, \
                                      u"Nombre de moustiquaires distribuées " \
                                      u"(femmes enceintes)", \
                                      attr='total_bednets_fe'),

    'total_cpn1_fe': ExcelFormField('M22', int, u"Nombre de CPN 1", \
                                                         attr='total_cpn1_fe'),
    'total_sp1_fe': ExcelFormField('M23', int, u"Nombre de SP1", \
                                                          attr='total_sp1_fe'),
    'total_sp2_fe': ExcelFormField('M24', int, u"Nombre de SP2", \
                                                          attr='total_sp2_fe'),

    'stockout_act_infant': ExcelFormField('M5', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Nourisson - Enfant", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_infant'),
    'stockout_act_kid': ExcelFormField('M6', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Grand Enfant", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_kid'),
    'stockout_act_adult': ExcelFormField('M7', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Adulte", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_adult'),
    'stockout_arthemether': ExcelFormField('M11', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"Arthemether", \
                                     cast_args=YN_MAP,
                                     attr='stockout_arthemether'),
    'stockout_quinine': ExcelFormField('M12', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"Quinine Injectable", \
                                     cast_args=YN_MAP,
                                     attr='stockout_quinine'),
    'stockout_serum': ExcelFormField('M13', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"Serum", \
                                     cast_args=YN_MAP,
                                     attr='stockout_serum'),
    'stockout_mild': ExcelFormField('M16', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"MILD", \
                                     cast_args=YN_MAP,
                                     attr='stockout_mild'),
    'stockout_rdt': ExcelFormField('M17', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"TDR", \
                                     cast_args=YN_MAP,
                                     attr='stockout_rdt'),
    'stockout_sp': ExcelFormField('M18', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"SP", \
                                     cast_args=YN_MAP,
                                     attr='stockout_sp'),
    'fillin_day': ExcelFormField('K28', \
                                 ExcelTypeConverter.NormalizedIntChoiceList, \
                                 u"Jour de remplissage", \
                                 cast_args=DAY_MAP),
    'fillin_month': ExcelFormField('L28', \
                                  ExcelTypeConverter.NormalizedIntChoiceList, \
                                  u"Mois de remplissage", \
                                  cast_args=MONTH_MAP),
    'fillin_year': ExcelFormField('M28', \
                                  ExcelTypeConverter.NormalizedIntChoiceList, \
                                  u"Année de remplissage", \
                                  cast_args=YEAR_MAP),
    'author': ExcelFormField('L26', unicode, \
                             u"Auteur du formulaire", attr='author'),
        }
    }

    def section_from_variable(self, variable):
        if variable.startswith('stockout_'):
            return 'stockout'
        last = variable.rsplit('_', 1)[-1]
        if last in ('u5', '5p', 'fe'):
            return last
        if variable in ('month', 'year'):
            return 'period'
        if variable in ('region', 'district', 'hc'):
            return 'location'
        if variable.startswith('fillin_') or variable in ('author',):
            return 'fillin'
        return None

    def missing_value(self, variable):
        self.errors.add("%s is missing." \
                                % self.mapping()[variable].display_name(), \
                                  self.section_from_variable(variable))

    def value_error(self, data, field, variable, exception):
        def clean_data(value):
            if isinstance(value, float) and value.is_integer():
                return int(value)
            return value

        self.errors.add("%s is not a valid data for %s" \
                        % (clean_data(data), field.display_name()), \
                           self.section_from_variable(variable))

    def is_complete(self):
        blank_fields = ('region', 'district')
        complete = True
        for fieldid in self.mapping():
            if fieldid in blank_fields:
                continue

            try:
                value = self.get(fieldid)
            except MissingData:
                self.missing_value(fieldid)
                complete = False

            if value == None:
                self.missing_value(fieldid)
                complete = False
        return complete

    def validate(self):

        no_more_than_text = "%(field2)s (%(f2value)d) can't be more " \
                            "than %(field1)s (%(f1value)d)"
        allcats = ('u5', '5p', 'fe')
        no5pcat = ('u5', 'fe')
        nofecat = ('u5', '5p')

        def test_value_under(fieldref, fieldtest, cats):
            for cat in cats:
                try:
                    dic = {'field2': self.field_name('%s_%s' \
                                                     % (fieldtest, cat)), \
                           'f2value': self.get('%s_%s' % (fieldtest, cat)), \
                           'field1': self.field_name('%s_%s' \
                                                     % (fieldref, cat)), \
                           'f1value': self.get('%s_%s' % (fieldref, cat))}
                    if dic['f1value'] < dic['f2value']:
                        self.errors.add(no_more_than_text % dic, cat)
                except MissingData:
                    # this missing data should have already been reported
                    pass

        # total > malaria cases
        test_value_under('total_consultation', 'total_malaria', allcats)

        # total >  malaria simple
        test_value_under('total_consultation', 'total_malaria_simple', nofecat)

        # total >  malaria severe
        test_value_under('total_consultation', 'total_malaria_severe', allcats)

        # suspected > malaria simple
        test_value_under('total_malaria', 'total_malaria_simple', nofecat)

        # suspected > malaria severe
        test_value_under('total_malaria', 'total_malaria_severe', allcats)

        # suspected > malaria tested
        test_value_under('total_malaria', 'total_malaria_tested', allcats)

        # suspected > malaria confirmed
        test_value_under('total_malaria', 'total_malaria_confirmed', allcats)

        # suspected > simple + severe
        for cat in nofecat:
            try:
                dic = {'field2': u"%s + %s" \
                       % (self.field_name('total_malaria_simple_%s' % cat), \
                          self.field_name('total_malaria_severe_%s' % cat)), \
                       'f2value': int(self.get('total_malaria_simple_%s' \
                                               % cat)) \
                                  + int(self.get('total_malaria_severe_%s' \
                                                 % cat)), \
                       'field1': self.field_name('total_malaria_%s' % cat), \
                       'f1value': self.get('total_malaria_%s' % cat)}
                if dic['f1value'] < dic['f2value']:
                    self.errors.add(no_more_than_text % dic, cat)
            except MissingData:
                pass

        # tested > confirmed
        test_value_under('total_malaria_tested', \
                         'total_malaria_confirmed', allcats)

        # tested > ACT
        test_value_under('total_malaria_tested', \
                         'total_malaria_acttreated', allcats)

        # confirmed > act
        test_value_under('total_malaria_confirmed', \
                         'total_malaria_acttreated', allcats)

        # total inpatient > malaria inpatient
        test_value_under('total_inpatient', 'total_malaria_inpatient', allcats)

        # total death > malaria death
        test_value_under('total_death', 'total_malaria_death', allcats)

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

    def create_report(self, author):
        period = MonthPeriod.find_create_from(year=self.get('year'), \
                                              month=self.get('month'))
        entity = Entity.objects.get(slug=self.get('hc'), type__slug='cscom')
        report = MalariaReport.create(period, entity, author)

        return report
