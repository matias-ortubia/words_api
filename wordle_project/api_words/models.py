from django.db import models

class Word(models.Model):
    # key = models.BigAutoField(primary_key=True, verbose_name="ID")
    word = models.CharField(max_length=30, verbose_name="Word")
    length = models.IntegerField(verbose_name="Length")
    language = models.CharField(max_length=5, verbose_name="Language")

    class Meta:
        managed = False
        db_table = 'words'

    def __str__(self):
        return self.word + " - " + self.language + " - " + str(self.length)