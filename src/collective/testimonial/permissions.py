# -*- coding: utf-8 -*-
from AccessControl.Permission import addPermission
from AccessControl.SecurityInfo import ModuleSecurityInfo

security = ModuleSecurityInfo('collective.testimonial')

TYPE_ROLES = ('Manager', 'Site Administrator', 'Owner', 'Contributor')
TYPES = ['Testimonial']

perms = []

for typename in TYPES:
    permid = 'Add' + typename
    permname = 'collective.testimonial: Add ' + typename
    security.declarePublic(permid)
    addPermission(permname, default_roles=TYPE_ROLES)

AddTestimonial = 'collective.artowrk: Add Testimonial'
