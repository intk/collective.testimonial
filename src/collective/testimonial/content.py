# -*- coding: utf-8 -*-

from collective.testimonial.interfaces import ITestimonial
from plone.app.contenttypes.interfaces import ILink
from plone.dexterity.content import Container, Item
from zope.interface import implementer

import six

@implementer(ILink)
class Testimonial(Item):
    """Convenience subclass for ``Testimonial`` portal type
    """
    
