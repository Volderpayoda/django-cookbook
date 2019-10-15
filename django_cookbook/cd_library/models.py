from django.db import models

# Create your models here.

genre_choices = (
    ('R', 'Rock'),
    ('B', 'Blues'),
    ('J', 'Jazz'),
    ('P', 'Pop')
)

class CD(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    artist = models.CharField(max_length=40)
    date = models.DateField()
    genre = models.CharField(max_length=1, choices=genre_choices)
    
    def __str__(self):
        return "%s by %s, %s" %(self.title, self.artist, self.date.year)
