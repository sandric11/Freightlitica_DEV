# Register your models here.
from django.contrib import admin
from .models import ltl
from .models import groupage, BP, FP, country_zone_postal

admin.site.register(ltl)
admin.site.register(groupage)
admin.site.register(BP)
admin.site.register(FP)
admin.site.register(country_zone_postal)
