from django.db import models
from django.urls import reverse, NoReverseMatch

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
       return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    name = models.CharField('Name', max_length=100)
    url = models.CharField(max_length=200, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    named_url = models.CharField(max_length=100, blank=True, help_text='Name of the URL pattern defined in urls.py')

    def get_absolute_url(self):
        if self.named_url:
            try:
                url = reverse(self.named_url)
            except NoReverseMatch:
                url = '#'
        else:
            url = self.url or '#'

        if url != '#' and not url.startswith(('http://', 'https://', '/')):
            url = '/' + url
        if url != '#' and url.startswith('/') and not url.endswith('/'):
            url = url + '/'
        return url

    def __str__(self):
       return self.name