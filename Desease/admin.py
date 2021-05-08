
from django.contrib import admin
from .models import user_registration
from .models import reg
from .models import feedback
# Register your models here.
admin.site.register(user_registration)
admin.site.register(reg)
admin.site.register(feedback)

