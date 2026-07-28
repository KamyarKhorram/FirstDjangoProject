from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=['-created_date']
        verbose_name='Category'
        verbose_name_plural='Categories'
    def __str__(self):
        return self.name

class Post(models.Model):
    image=models.ImageField(upload_to='blog/', default='blog/default.jpg')

    # author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True) SET_NULL => if the related User is deleted, keep the Post but set author to NULL
    # (requires null=True since the field must be able to hold no value)

    author=models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE => if the related User is deleted, delete this Post too
    # (no null=True needed, since the Post can't exist without an author)

    title=models.CharField(max_length=100)
    content=models.TextField()

    # tag

    category=models.ManyToManyField('Category')

    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False) # field always has a value, starts as False if not provided
    published_date=models.DateTimeField(null=True) # this field is allowed to be empty
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
    def __str__(self): # str dunder method: returns a readable string representation of the object
        # return " {} - {} ".format(self.title, self.id)
        return f" {self.title} - {self.id} "