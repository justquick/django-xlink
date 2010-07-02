from django.contrib import admin
from models import Query, Result

class QueryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','search_on','look_for','active')
    list_editable = list_display[1:]
    search_fields = ('search_on','look_for')
    
class ResultAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','found_on','timestamp','display')
    list_editable = ('display',)
    search_fields = ('url','found_on')    
    list_filter = ('timestamp','display')
    
admin.site.register(Query, QueryAdmin)
admin.site.register(Result, ResultAdmin)
