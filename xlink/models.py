from django.db import models

class Query(models.Model):
    search_on = models.URLField(help_text='URL to comb through looking for links')
    look_for = models.CharField(max_length=100, help_text='Domain name of the site you wish to search for, usually your own')
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.search_on
    
class Result(models.Model):
    url = models.URLField(help_text='URL found on external site')
    found_on = models.URLField(help_text='URL of external site where link was found')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.url