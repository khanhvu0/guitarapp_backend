from djongo import models

# Create your models here.

class ImgLink(models.Model):
    link = models.CharField(max_length = 200)

    class Meta:
        abstract = True


class ChordImages(models.Model):
    chord_name = models.CharField(max_length=10, primary_key=True)
    images = models.ArrayField(
        model_container=ImgLink,
    )

