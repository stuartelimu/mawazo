from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content",)
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title", "class": "form-control"}),
            "content": forms.Textarea(attrs={"placeholder": "Share your thoughts...", "class": "editable medium-editor-textarea form-control"}),
        }
        labels = {
            "title": "",
            "content": "",
        }
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(attrs={"class": "editable medium-editor-textarea form-control"})
        }
        labels = {
            "content": "",
        }
        
        