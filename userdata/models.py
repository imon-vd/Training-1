from django.db import models

"""
    Every time you create/modify a model ,
    you will be required to make migrations and apply those migrations.
    Understand what is a migration from here : https://docs.djangoproject.com/en/4.0/topics/migrations/
    
    Use commands : `python manage.py makemigrations` to create migrations
    and `python manage.py migrate` to apply those migrations 
"""

# Create your models here.
class UserData(models.Model):
    # This field stores the creation date.
    created_at = models.DateTimeField(auto_now_add=True)
    # This field stores the name
    name = models.CharField(max_length=50,null=True,blank=True)
    # Rest Fields are missing. Make sure to add all of them.
    
    # You have come accross an inbuilt methods/dunder methods.
    # Read more about them here : 
    def __str__(self):
        """
        This function is used to return a string representation of the object.
        https://www.tutorialsteacher.com/python/magic-methods-in-python
        """
        return self.name
        # Modify this return in such a way that it should show something like this:
        # Name : city( if city is there , if not only Name with no :)
        # Example 1:  Imon Roy : Kolkata , Imon's entry had a city so it should be name : city.
        # Example 2: Vishal , vishal's entry didn't have a city so it would just have their name.      
        