from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length = 100)
    price = models.BigIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length = 100)

    # TODO: Добавьте требуемые поля
   
    def __str__(self):
        return self.name