from django.db import models

# Create your models here.

class Search(models.Model):

    search = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.search
    
    class Meta:
        verbose_name_plural = 'searches' # how model name should look like in admin panel with it is plural