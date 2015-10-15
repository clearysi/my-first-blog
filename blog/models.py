from django.db import models
from django.utils import timezone


# Create your models here.
# This line defines our model. class indicates we are defining an object.
# Post is the name of our model, always starts with an uppercase.
# Models.model means that the Post is a Django model, so django knows it should be saved in the database.
class Post(models.Model):
    author = models.ForeignKey('auth.User')  # this is a link to another model
    title = models.CharField(max_length=200)  # This is how you define text with a limited number of characters
    text = models.TextField()  # This is for long text without a limit.
    created_date = models.DateTimeField(blank=True, null=True)  # This is a date and time.
    published_date=models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
