from django import forms
from .models import Comment, Post, Category

categories = Category.objects.all().values_list('name', 'name') #name porque le dimos ese nombre en models
categories_list = []

for category in categories:
    categories_list.append(category)


class PostForm(forms.ModelForm): #Esta clase nos permite crear nuestro propio formulario
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'preview', 'body', 'header_image') #Deben ser las mismas que tenemos definidas en nuestro modelo
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices = categories_list, attrs={'class':'form-control'}),
            'preview': forms.Textarea(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        } # Podemos utilizar un placeholder:stuff para los inputs

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author', 'category', 'preview', 'body', 'header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices = categories_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'preview': forms.Textarea(attrs={'class':'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }