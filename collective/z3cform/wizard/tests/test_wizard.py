# -*- coding: utf-8 -*-

import unittest

from collective.z3cform.wizard import wizard
from collective.z3cform.wizard.tests import tests
from z3c.form import field
from zope.component import getGlobalSiteManager
from zope.interface import Interface
from zope.interface import alsoProvides
from zope.interface import implements
from zope import schema


class ITestForm(Interface):

    field_one = schema.TextLine(title=u'one')
    field_two = schema.TextLine(title=u'two')
    field_three = schema.TextLine(title=u'three')


class TestStepOne(wizard.Step):
    fields = field.Fields(ITestForm).select('field_one')


class TestStepTwo(wizard.Step):
    fields = field.Fields(ITestForm).select('field_two')
    condition = 'test'


class TestStepThree(wizard.Step):
    fields = field.Fields(ITestForm).select('field_three')


class TestWizard(wizard.Wizard):
    steps = (
        TestStepOne,
        TestStepTwo,
        TestStepThree,
    )


class ConditionAdapter(object):
    implements(wizard.IStepCondition)

    def __init__(self, context, request, wizard):
        self.context = context
        self.request = request
        self.wizard = wizard

    def validate(self):
        return True


class TestWizardCondition(unittest.TestCase):

    def setUp(self):
        tests.setUp(self)
        context = type('context', (object, ), {})()
        alsoProvides(context, Interface)
        self.wizard = TestWizard(context, tests.TestRequest())

    def test_wizard_condition(self):
        gsm = getGlobalSiteManager()
        gsm.registerAdapter(
            ConditionAdapter,
            (Interface, Interface, Interface),
            wizard.IStepCondition,
            'test',
        )
        self.wizard.updateActiveSteps()
        self.assertEqual(3, len(self.wizard.activeSteps))

        def _validate(self):
            return False

        ConditionAdapter.validate = _validate
        self.wizard.updateActiveSteps()
        self.assertEqual(2, len(self.wizard.activeSteps))
        self.assertTrue(TestStepTwo not in self.wizard.activeSteps)
