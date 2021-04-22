from django.contrib import admin

from chatBackend.models import groups
from chatBackend.models import messages
from chatBackend.models import persons

# Register your models here.

admin.site.register(persons)
admin.site.register(groups)
admin.site.register(messages)