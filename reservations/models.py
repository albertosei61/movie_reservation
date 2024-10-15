from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    poster_image = models.ImageField(upload_to='posters/')
    
    def __str__(self):
        return self.title

class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.title} at {self.showtime}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} reserved seat {self.seat_number} for {self.showtime}"
    



