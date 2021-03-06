from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(blank=True,default='1.jpg')
    def publish(self,user):
        usr = User
        self.author = user
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)
    def get_absolute_url(self):
        return reverse('myblog:post_detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post = models.ForeignKey('myblog.Post',related_name='comments')
    author = models.CharField(max_length=128)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)
    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')
