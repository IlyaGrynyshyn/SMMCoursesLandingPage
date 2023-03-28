from django.db import models


class Pre_Registration(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я")
    phone = models.CharField(max_length=21, verbose_name='Номер телефону')
    email = models.EmailField(verbose_name='Пошта')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Передзапис'
        verbose_name_plural = 'Передзапис'
