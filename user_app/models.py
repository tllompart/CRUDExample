from django.db import models
from django.urls import reverse

# Create your models here.
class UserAcount(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    IBAN = models.CharField(max_length=14)
    created_by = models.CharField(max_length=14)

    def __str__(self):
        return self.first_name + ' '+ self.last_name
    
    def get_absolute_url(self):
        
        return reverse('user_app:user_account_edit', kwargs={'pk': self.pk})