from django.db import models

class Customer(models.Model):
    customer_name=models.CharField(max_length=255)
    customer_review=models.TextField()
    
    def __str__(self):
        return self.customer_name
