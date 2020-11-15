from django.contrib import admin
# from myapp.models import UserProfileInfo, User
# # Register your models here.

# admin.site.register(UserProfileInfo)

from django.contrib import admin
from myapp.models import login, training, candidate, Register
# Register your models here.
admin.site.register(login)
admin.site.register(training)
admin.site.register(candidate)
admin.site.register(Register)
