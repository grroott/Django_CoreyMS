from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
	comment = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder':'Enter your thoughts here!','rows':3, 'cols':50}))
	class Meta:
		model = Comment
		fields = ['comment']