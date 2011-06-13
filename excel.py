#!/usr/bin/env python
# encoding=utf-8
# maintainer: rgaudin

from bolibana_reporting.excel import (ExcelForm, ExcelFormField, \
                                      ExcelTypeConverter)
from bolibana_reporting.models import Period, MonthPeriod, Entity
from pnlp_core.models import MalariaReport
from pnlp_core.validator import MalariaReportValidator


class MalariaExcelForm(ExcelForm):

    YN_MAP = {'oui': MalariaReport.YES, 'non': MalariaReport.NO, '': None, None:None}
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

    'u5_total_consultation_all_causes': ExcelFormField('C7', int, \
                    u"Total consultation, toutes causes confondues", \
                    attr='total_consult_u5'),
    'o5_total_consultation_all_causes': ExcelFormField('E7', int, \
                u"Total consultation, toutes causes confondues", \
                attr='total_consult_5p'),
    'pw_total_consultation_all_causes': ExcelFormField('G7', int, \
                                        u"Total consultation, toutes causes " \
                                        "confondues", \
                                         attr='total_consult_fe'),

    'u5_total_suspected_malaria_cases': ExcelFormField('C8', int, \
                       u"Nbre de Cas de paludisme (Tous suspectés)", \
                       attr='total_malaria_u5'),
    'o5_total_suspected_malaria_cases': ExcelFormField('E8', int, \
                   u"Nbre de Cas de paludisme (Tous suspectés)", \
                   attr='total_malaria_5p'),
    'pw_total_suspected_malaria_cases': ExcelFormField('G8', int, \
             u"Nbre de Cas de paludisme (Tous suspectés)", \
             attr='total_malaria_fe'),

    'u5_total_simple_malaria_cases': ExcelFormField('C9', int, \
                                 u"Nbre de Cas de paludisme Simple", \
                                 attr='total_malaria_simple_u5'),
    'o5_total_simple_malaria_cases': ExcelFormField('E9', int, \
                             u"Nbre de Cas de paludisme Simple", \
                             attr='total_malaria_simple_5p'),

    'u5_total_severe_malaria_cases': ExcelFormField('C10', int, \
                                  u"Nbre de Cas de paludisme Grave", \
                                  attr='total_malaria_severe_u5'),
    'o5_total_severe_malaria_cases': ExcelFormField('E10', int, \
                              u"Nbre de Cas de paludisme Grave", \
                              attr='total_malaria_severe_5p'),
    'pw_total_severe_malaria_cases': ExcelFormField('G10', int, \
                        u"Nbre de Cas de paludisme Grave", \
                        attr='total_malaria_severe_fe'),

    'u5_total_tested_malaria_cases': ExcelFormField('C11', int, \
                          u"Cas de paludisme testés (GE et/ou TDR)", \
                          attr='total_malaria_tested_u5'),
    'o5_total_tested_malaria_cases': ExcelFormField('E11', int, \
                      u"Cas de paludisme testés (GE et/ou TDR)", \
                      attr='total_malaria_tested_5p'),
    'pw_total_tested_malaria_cases': ExcelFormField('G11', int, \
                                         u"Cas de paludisme testés " \
                                         "(GE et/ou TDR)", \
                                         attr='total_malaria_tested_fe'),

    'u5_total_confirmed_malaria_cases': ExcelFormField('C12', int, \
                       u"Cas de paludisme confirmés (GE et/ou TDR)", \
                       attr='total_malaria_confirmed_u5'),
    'o5_total_confirmed_malaria_cases': ExcelFormField('E12', int, \
                   u"Cas de paludisme confirmés (GE et/ou TDR)", \
                   attr='total_malaria_confirmed_5p'),
    'pw_total_confirmed_malaria_cases': ExcelFormField('G12', int, \
                                         u"Cas de paludisme confirmés " \
                                         "(GE et/ou TDR)", \
                                         attr='total_malaria_confirmed_fe'),

    'u5_total_treated_malaria_cases': ExcelFormField('C13', int, \
                                    u"Nbre de Cas traités avec CTA", \
                                    attr='total_malaria_acttreated_u5'),
    'o5_total_treated_malaria_cases': ExcelFormField('E13', int, \
                                u"Nbre de Cas traités avec CTA", \
                                attr='total_malaria_acttreated_5p'),
    'pw_total_treated_malaria_cases': ExcelFormField('G13', int, \
                          u"Nbre de Cas traités avec CTA", \
                          attr='total_malaria_acttreated_fe'),

    'u5_total_inpatient_all_causes': ExcelFormField('C17', int, \
                                    u"Total Hospitalisés Paludisme", \
                                    attr='total_malaria_inpatient_u5'),
    'o5_total_inpatient_all_causes': ExcelFormField('E17', int, \
                                u"Total Hospitalisés Paludisme", \
                                attr='total_malaria_inpatient_5p'),
    'pw_total_inpatient_all_causes': ExcelFormField('G17', int, \
                          u"Total Hospitalisés Paludisme", \
                          attr='total_malaria_inpatient_fe'),

    'u5_total_malaria_inpatient': ExcelFormField('C18', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_u5'),
    'o5_total_malaria_inpatient': ExcelFormField('E18', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_5p'),
    'pw_total_malaria_inpatient': ExcelFormField('G18', int, \
                                     u"Total Hospitalisations toutes causes " \
                                     u"confondues", \
                                     attr='total_inpatient_fe'),

    'u5_total_death_all_causes': ExcelFormField('C22', int, \
                                     u"Cas de décès pour paludisme", \
                                     attr='total_malaria_death_u5'),
    'o5_total_death_all_causes': ExcelFormField('E22', int, \
                                 u"Cas de décès pour paludisme", \
                                 attr='total_malaria_death_5p'),
    'pw_total_death_all_causes': ExcelFormField('G22', int, \
                           u"Cas de décès pour paludisme", \
                           attr='total_malaria_death_fe'),

    'u5_total_malaria_death': ExcelFormField('C23', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_u5'),
    'o5_total_malaria_death': ExcelFormField('E23', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_5p'),
    'pw_total_malaria_death': ExcelFormField('G23', int, \
                                         u"Total cas de décès toutes causes " \
                                         u"confondues", \
                                         attr='total_death_fe'),

    'u5_total_distributed_bednets': ExcelFormField('C27', int, \
                                      u"Nombre de moustiquaires distribuées " \
                                      u"(< 5ans)", attr='total_bednets_u5'),
    'pw_total_distributed_bednets': ExcelFormField('E27', int, \
                                      u"Nombre de moustiquaires distribuées " \
                                      u"(femmes enceintes)", \
                                      attr='total_bednets_fe'),

    'pw_total_anc1': ExcelFormField('M22', int, u"Nombre de CPN 1", \
                                                         attr='total_anc1_fe'),
    'pw_total_sp1': ExcelFormField('M23', int, u"Nombre de SP1", \
                                                          attr='total_sp1_fe'),
    'pw_total_sp2': ExcelFormField('M24', int, u"Nombre de SP2", \
                                                          attr='total_sp2_fe'),

    'stockout_act_children': ExcelFormField('M5', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Nourisson - Enfant", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_children'),
    'stockout_act_youth': ExcelFormField('M6', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Grand Enfant", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_youth'),
    'stockout_act_adult': ExcelFormField('M7', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"CTA Adulte", \
                                     cast_args=YN_MAP,
                                     attr='stockout_act_adult'),
    'stockout_arthemeter': ExcelFormField('M11', \
                                     ExcelTypeConverter.NormalizedChoiceList, \
                                     u"Arthemether", \
                                     cast_args=YN_MAP,
                                     attr='stockout_arthemeter'),
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
    'stockout_bednet': ExcelFormField('M16', \
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
        last = variable.split('_', 1)[0]
        if last in ('u5', 'o5', 'pw'):
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
        validator = MalariaReportValidator(self)
        validator.validate()
        self.errors.fusion(validator.errors)

    def fields_for(self, cat):
        u5fields = ['u5_total_consultation_all_causes', \
                    'u5_total_suspected_malaria_cases', \
                    'u5_total_simple_malaria_cases', \
                    'u5_total_severe_malaria_cases', \
                    'u5_total_tested_malaria_cases', \
                    'u5_total_confirmed_malaria_cases', \
                    'u5_total_treated_malaria_cases', \
                    'u5_total_inpatient_all_causes', \
                    'u5_total_malaria_inpatient', \
                    'u5_total_death_all_causes', \
                    'u5_total_malaria_death', \
                    'u5_total_distributed_bednets']
        if cat == 'u5':
            return u5fields
        if cat == 'o5':
            return [f.replace('u5', 'o5') for f in u5fields][:-1]
        if cat == 'pw':
            fields = [f.replace('u5', 'pw') for f in u5fields]
            fields.remove('pw_total_simple_malaria_cases')
            fields.extend(['pw_total_anc1', 'pw_total_sp1', 'pw_total_sp2'])
            return fields
        if cat == 'so':
            return ['stockout_act_children', \
                    'stockout_act_youth', \
                    'stockout_act_adult', \
                    'stockout_arthemeter', \
                    'stockout_quinine', \
                    'stockout_serum', \
                    'stockout_bednet', \
                    'stockout_rdt', \
                    'stockout_sp']

    def data_for_cat(self, cat, as_dict=False):
        data = []
        for field in self.fields_for(cat):
            data.append(self.get(field))
        return data

    def create_report(self, author):
        period = MonthPeriod.find_create_from(year=self.get('year'), \
                                              month=self.get('month'))
        entity = Entity.objects.get(slug=self.get('hc'), type__slug='cscom')
        report = MalariaReport.start(period, entity, author, \
                                     type=MalariaReport.TYPE_SOURCE)

        report.add_underfive_data(*self.data_for_cat('u5'))
        report.add_overfive_data(*self.data_for_cat('o5'))
        report.add_pregnantwomen_data(*self.data_for_cat('pw'))
        report.add_stockout_data(*self.data_for_cat('so'))
        report.save()

        return report
