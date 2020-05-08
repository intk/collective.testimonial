
# -*- coding: utf-8 -*-
from AccessControl.SecurityManagement import getSecurityManager
from datetime import datetime
from DateTime import DateTime
from plone.app.dexterity import _
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.app.z3cform.widget import DatetimeFieldWidget
from plone.app.z3cform.widget import SelectFieldWidget
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.dexterity.utils import safe_unicode
from plone.supermodel import model
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from six.moves import map
from z3c.form.interfaces import IAddForm
from z3c.form.interfaces import IEditForm
from z3c.form.widget import ComputedWidgetAttribute
from zope import schema
from zope.component import adapter
from zope.component.hooks import getSite
from zope.interface import Invalid
from zope.interface import invariant
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory
from zope.schema.interfaces import ISequence
from zope.schema.interfaces import IText

import six

from plone.app.dexterity.behaviors.metadata import MetadataBase

@provider(IFormFieldProvider)
class ITestimonial(model.Schema):

    # categorization fieldset
    model.fieldset(
        'testimonial',
        label=_(u'label_schema_testimonial', default=u'Testimonial'),
        fields=['person'],
    )

    person = schema.TextLine(
        title=_(u'label_person', default=u'Person'),
        required=False
    )


    



    









