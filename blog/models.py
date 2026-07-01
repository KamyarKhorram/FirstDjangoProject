from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title=models.CharField(max_length=100)
    content=models.TextField()
    # tag
    # category
    counted_views=models.IntegerField(default=0)
    status=models.BooleanField(default=False) # field always has a value, starts as False if not provided
    published_date=models.DateTimeField(null=True) # this field is allowed to be empty
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
        # verbose_name='پست'
        # verbose_name_plural='پست ها'
    def __str__(self): # str dunder method: returns a readable string representation of the object
        # return " {} - {} ".format(self.title, self.id)
        return f" {self.title} - {self.id} "