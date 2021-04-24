from django.contrib import admin

from chatBackend.models import groups
from chatBackend.models import messages
from chatBackend.models import persons

# Register your models here.

#admin.site.register(persons)


@admin.register(persons)
class personsAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'birthdate', 'email', 'full_name']
    list_filter = ('created_at',)
    search_fields = ['nickname', 'email', 'full_name']

@admin.register(groups)
class groupsAdmin(admin.ModelAdmin):
    list_display = ['group_name', 'created_at']
    list_filter = ('created_at',)
    search_fields = ['person', 'group_name']

@admin.register(messages)
class messagesAdmin(admin.ModelAdmin):
    list_display = ['message', 'messageFrom', 'messageTo', 'created_at']
    list_filter = ('created_at', 'messageFrom', 'messageTo', 'viewed')
    search_fields = ['person', 'group_name']