from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Post, Tag
from taggit.forms import TagWidget

class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'})
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  
        widgets = {
            "tags": TagWidget(),
        }


    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tags_str = self.cleaned_data.get("tags", "")
        tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance
