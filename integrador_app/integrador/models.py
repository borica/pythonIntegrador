from django.db import models

# Create your models here.
class Produto():
    vg_name = models.CharField(max_length = 200)
    #vg_name = models.CharField(max_length = 200)
    #pub_date = models.DateTimeField('Publicado em')
    #vg_year = models.IntegerField(default=1950)
    #vg_fabricante = models.CharField(max_length = 200)
    #vg_vende = models.BooleanField(default=True)

