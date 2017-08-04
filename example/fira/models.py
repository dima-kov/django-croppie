from django.db import models


class Fira(models.Model):
    name = models.CharField(
        max_length=255,
    )
    image = models.ImageField(
        upload_to='fira',
    )

    class Meta:
        verbose_name = "Fira"
        verbose_name_plural = "Firas"

    def __str__(self):
        return self.name

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('')
