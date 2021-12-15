from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm): #Esta clase nos permite crear nuestro propio formulario
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'preview', 'body', 'tag', 'header_image') #Deben ser las mismas que tenemos definidas en nuestro modelo
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
            'preview': forms.Textarea(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'tag': forms.TextInput(attrs={'class':'form-control'}),
        } # Podemos utilizar un placeholder:stuff para los inputs

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category', 'preview', 'body', 'header_image') #Deben ser las mismas que tenemos definidas en nuestro modelo
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
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