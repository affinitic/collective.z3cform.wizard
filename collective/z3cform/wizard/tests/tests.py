# -*- coding: utf-8 -*-

from z3c.form.datamanager import DictionaryField
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.component import testing, provideAdapter
from zope.configuration import xmlconfig
from zope.interface import implements
from zope.testing.doctest import DocFileSuite

import Products.statusmessages
import ZPublisher
import doctest
import plone.z3cform.tests
import unittest
import z3c.form
import z3c.form.testing
import zope.browserresource
import zope.component
import zope.i18n
import zope.security


def setUp(test):
    testing.setUp(test)
    z3c.form.testing.setupFormDefaults()
    plone.z3cform.tests.setup_defaults()
    provideAdapter(DictionaryField)
    xmlconfig.XMLConfig('meta.zcml', zope.component)()
    xmlconfig.XMLConfig('meta.zcml', zope.security)()
    xmlconfig.XMLConfig('meta.zcml', zope.i18n)()
    xmlconfig.XMLConfig('meta.zcml', z3c.form)()
    xmlconfig.XMLConfig('meta.zcml', zope.browserresource)()
    xmlconfig.XMLConfig('configure.zcml', zope.i18n)()
    xmlconfig.XMLConfig('configure.zcml', z3c.form)()
    xmlconfig.XMLConfig('i18n.zcml', ZPublisher)()
    xmlconfig.XMLConfig('configure.zcml', Products.statusmessages)()


class MockSession(dict):
    def set(self, key, value):
        self[key] = value


class TestRequest(z3c.form.testing.TestRequest):
    implements(IAttributeAnnotatable)

    def __init__(self, **kw):
        z3c.form.testing.TestRequest.__init__(self, **kw)
        self.SESSION = MockSession()


def test_suite():
    files = ['../wizard.txt', '../dynamic_wizard.txt']
    suites = [
        DocFileSuite(
            file,
            setUp=setUp,
            tearDown=testing.tearDown,
            optionflags=(doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
            globs=globals(),
        )
        for file in files]
    return unittest.TestSuite(suites)

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
