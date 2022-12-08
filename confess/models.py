from django.db import models

class confess(models.Model):
    confession = models.TextField(verbose_name='Confession')
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.confession


