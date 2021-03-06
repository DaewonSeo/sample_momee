from django.forms import ModelForm
from app.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'text']

