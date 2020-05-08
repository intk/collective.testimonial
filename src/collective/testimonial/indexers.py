# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from plone.app.contenttypes.interfaces import ILink

@indexer(ILink)
def testimonial_id(object, **kw):
    try:
        testimonial_id = getattr(object, 'testimonial_id', '')      
        return testimonial_id
    except:
        return ""

