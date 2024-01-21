from django.contrib import admin
from .models import (
    Team,
    Work,
    Form,
)

admin.site.register(Team)
admin.site.register(Work)
admin.site.register(Form)