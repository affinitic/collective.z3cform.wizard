# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.4.9dev'

DOCTESTS_PATH = os.path.join('collective', 'z3cform', 'wizard')

long_description = '\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
    open(os.path.join(DOCTESTS_PATH, 'wizard.txt')).read(),
    open(os.path.join(DOCTESTS_PATH, 'dynamic_wizard.txt')).read(),
])

setup(
    name='collective.z3cform.wizard',
    version=version,
    description=(
        "This is a library for creating multi-page wizards using "
        "z3c.form. Values are stored in a session until the wizard is "
        "finished."
    ),
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Zope2',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ],
    keywords='z3c.form wizard session',
    author='David Glick',
    author_email='davidglick@groundwire.org',
    url='https://github.com/collective/collective.z3cform.wizard/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.z3cform'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.z3cform>=0.7.5',
        'Products.statusmessages',
        'Zope2',
    ],
    extras_require=dict(
        test=[
            'plone.autoform',
            'plone.z3cform [test]',
            'z3c.form [test]',
        ],
        autowizard=[
            'plone.autoform',
        ],
    ),
    entry_points="""
    # -*- Entry points: -*-
    """,
)
