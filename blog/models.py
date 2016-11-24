from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comment(models.Model):
    #post = models.ForeignKey('blog.Post', related_name='comments')
    sender = models.EmailField()
    author = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #approved_comment = models.BooleanField(default=True)

    def publish(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
