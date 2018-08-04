from django.db import models
from provider.models import Provider

class CategoryProduct(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    TYPE_CHOICE = (
        ('drinks', "Bebida"),
        ('food', "Comida"),
        ('candy', "Doce"),
    )

    name = models.CharField("Nome",max_length=150)
    description = models.TextField("Descrição",blank=True)
    value = models.DecimalField("Valor",max_digits=10, decimal_places=2)
    products_type = models.CharField("Tipo do Produto",max_length=10, choices=TYPE_CHOICE, default='food')
    category = models.ForeignKey(CategoryProduct, on_delete=False, null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=False, null=True, blank=True)

    class Meta:
        verbose_name = "Produto"

    def __str__(self):
        return "{0} / {1} / {2}".format(self.name, self.value, self.description)




