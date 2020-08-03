from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=108)
    text = models.TextField(max_length=2064)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Returns title of a blog post in a string. """
        if len(self.title) < 52:
            return self.title
        else:
            return f"{self.title[:52]}..."