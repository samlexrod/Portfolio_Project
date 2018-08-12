from django.db import models

# Create A Blog model
    # title
    # pub_date
    # body
    # image

class Blog(models.Model):
    objects = object
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # to name the blogs in the admin page
    def __str__(self):
        return self.title

    # to provide with a summary in the allblogs
    def summary(self):
        return self.body[:100]

    # to cut the time from the timestamp
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

# Add the Blog app to the settings
    # In settings.py INSTALLED_APPS add
        # blog.appBlogConfig

# Create a migration
    # In terminal
        # python manage.py makemigrations
# Migrate
    # In terminal
        # python manage.py migrate


# Add the admin
    # In admin.py
        # from .models import Blog
        # admin.site.register(Blog)
