from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from genre.models import Mpttapp

# Register your models here.
admin.site.register(Mpttapp, DraggableMPTTAdmin)