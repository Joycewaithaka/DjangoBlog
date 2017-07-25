from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
      author = models.CharField( max_length = 30)
      title = models.CharField( max_length = 30)
      content = models.TextField()
      Timestamp = models.DateTimeField(auto_now =True)
      
      def __unicode__(self):
          return (self.author)
          
class Salon(models.Model):
      Styles =models.CharField( max_length =30)
      Services = models.TextField( max_length = 100)
      TimeAvailable = models.DateField(max_length =50)
      Pub_date =models.DateTimeField('date published')
      