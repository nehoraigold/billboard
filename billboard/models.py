from django.db import models

# Create your models here.
class Billboard(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    date_published = models.DateField("date published")

    def __str__(self):
        return '"{}" by {}'.format(self.title, self.author)


class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    author = models.CharField(max_length=150)
    date = models.DateField('comment date')
    billboard = models.ForeignKey(Billboard, on_delete=models.CASCADE, related_name="comments")

def get_recent_posts():
    posts = Billboard.objects.all()
    return posts