from django.contrib import admin

from .models import *

admin.site.register(Transaction)
admin.site.register(IOU)

class InlineParticipant(admin.TabularInline):
    model = Participant
    extra = 1

class SploodlAdmin(admin.ModelAdmin):
    inlines = [InlineParticipant]


admin.site.register(Sploodl, SploodlAdmin)