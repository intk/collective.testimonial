# -*- coding: utf-8 -*-
from BTrees.IIBTree import intersection
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.vocabularies import SlicableVocabulary
from plone.app.vocabularies.terms import BrowsableTerm
from plone.app.vocabularies.terms import safe_encode
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from plone.app.vocabularies.utils import parseQueryString
from plone.memoize.instance import memoize
from plone.registry.interfaces import IRegistry
from plone.uuid.interfaces import IUUID
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.ZCTextIndex.ParseTree import ParseError
from zope.browser.interfaces import ITerms
from zope.component import queryUtility
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.interfaces import ISource
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.site.hooks import getSite

import itertools
import os
import six
import warnings

"""@implementer(IVocabularyFactory)
class CountryVocabulary(object):
    
    keyword_index = 'country'

    def all_countries(self, kwfilter):
        site = getSite()
        self.catalog = getToolByName(site, 'portal_catalog', None)
        if self.catalog is None:
            return SimpleVocabulary([])
        index = self.catalog._catalog.getIndex(self.keyword_index)
        return safe_simplevocabulary_from_values(index._index, query=kwfilter)


    def __call__(self, context, query=None):
        return self.all_countries(query)

CountryVocabularyFactory = CountryVocabulary()"""

