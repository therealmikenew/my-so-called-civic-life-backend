from django.contrib import admin
from .models import User, Legislation, Action

# Register your models here.

admin.site.register(User)
admin.site.register(Legislation)
admin.site.register(Action)
