from django.db import models

class BlogTopic(models.Model):
    topic = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic

class BlogPost(models.Model):
    """ Model to control a blog post. """
    topic = models.ForeignKey(BlogTopic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """ Returns string of text attribute. """
        if len(self.text) > 52:
            return f"{self.text[:52]}..."
        else:
            return self.text