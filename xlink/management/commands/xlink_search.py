from django.core.management.base import BaseCommand
from django.core.exceptions import ImproperlyConfigured
try:
    from lxml.html import parse
except ImportError:
    raise ImproperlyConfigured('You must have lxml installed before searching')

from xlink.models import Query, Result

class Command(BaseCommand):
    def handle(self, *args, **options):
        for query in Query.objects.filter(active=True):
            
            html = parse(query.search_on).getroot()
            html.make_links_absolute(query.search_on)
            for link in html.iterlinks():
                try:
                    url = link[2]
                    domain = url.split('/')[2]
                except IndexError:
                    continue
                if domain == query.look_for:
                    lookup = {'url':url, 'found_on': query.search_on}
                    try:
                        Result.objects.filter(**lookup)[0]
                    except IndexError:
                        Result.objects.create(**lookup)

