from django.contrib import admin
from models import Query, Result

class QueryAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','search_on','look_for','active')
    list_editable = list_display[1:]
    search_fields = ('search_on','look_for')
    
class ResultAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','url','found_on','timestamp')
    list_editable = ('url',)
    search_fields = ('url','found_on')    
    list_filter = ('timestamp',)
    
admin.site.register(Query, QueryAdmin)
admin.site.register(Result, ResultAdmin)
