from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete elimina todas las publicaciones realizadas por User si el mismo es eliminado
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    preview = RichTextField(blank=True, null=True) # O podemos usar un filtro en el html e.g. {{post.body|slice:'125'}}
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author) #Para mostrar el titulo y el autor
    
    def get_absolute_url(self):
        return reverse('home') #args=(str(self.id)))
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)# Quiere decir que si un post es eliminado, sus comentarios tambien
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse('home')