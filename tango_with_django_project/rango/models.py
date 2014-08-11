from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

# CharField, a field for storing character data (e.g. strings). Specify max_length to provide a maximum number of characters the field can store.
# URLField, much like a CharField, but designed for storing resource URLs. You may also specify a max_length parameter.
# IntegerField, which stores integers.
# DateField, which stores a Python datetime.date.