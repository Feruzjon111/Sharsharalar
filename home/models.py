from django.db import models

class Sharshara(models.Model):
    nomi = models.CharField(max_length=100)
    joylashuv = models.CharField(max_length=200)
    tavsif = models.TextField()
    rasm = models.ImageField(upload_to='sharsharalar/')
    xarita_iframe = models.TextField(help_text="Google Maps iframe kodini joylang")

    def __str__(self):
        return self.nomi
