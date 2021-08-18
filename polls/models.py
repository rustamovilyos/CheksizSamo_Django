from django.db import models
# from audiofield.fields import AudioField


class Janrlar(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class Kitoblar(models.Model):
    nomi = models.CharField(max_length=100)
    janri = models.ForeignKey(Janrlar, null=True, on_delete=models.CASCADE)
    muallif = models.CharField(max_length=50)
    fayl = models.FileField(upload_to='media/doc/')
    nashr_yili = models.IntegerField(null=True)
    rasm = models.ImageField(null=True, blank=True)
    audio = models.FileField(upload_to='media/audio/', null=True, blank=True)
    sahifalar = models.IntegerField(null=True)
    kitob_haqida = models.TextField(null=True)

    def __str__(self):
        back = self.nomi
        return back
