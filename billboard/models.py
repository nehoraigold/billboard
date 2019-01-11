from django.db import models

# Create your models here.
class Billboard(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    date_published = models.DateField("date published")

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


def get_recent_posts():
    posts = Billboard.objects.all()
    return posts