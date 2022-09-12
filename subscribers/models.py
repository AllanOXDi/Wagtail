from django.db import models


class Subscribers(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')
    profile_image = models.ImageField(upload_to='profile_images', blank=True, help_text='Profile image')

    def __str__(self):

        return self.full_name

    class Meta:  # noqa
        verbose_name = "Susbcriber"
        verbose_name_plural = "Subscribers"
