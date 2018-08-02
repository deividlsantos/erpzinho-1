from django.db import models

class Provider(models.Model):


    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table='provider'
        verbose_name = "Fornecedor"

    def __str__(self):
        return "{0} / {1} ".format(self.name, self.description)