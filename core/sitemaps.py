from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    # List all named static views here
    def items(self):
        # Add all named URLs you want to include
        return [
            'home',
            'what-is-edpi-in-gaming', 
        ]

    def location(self, item):
        return reverse(item)