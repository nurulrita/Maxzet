from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserProfile)
admin.site.register(Men)
admin.site.register(Women)
admin.site.register(TransaksiMen)
admin.site.register(TransaksiWomen)
