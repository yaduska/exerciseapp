from django import forms
from .models import Community,Message

class CommunityForm(forms.ModelForm):
    class Meta:
        model=Community
        fields=('topic',)
        widgets={
            'topic':forms.TextInput(attrs={'class':'w-1/2 px-6 py-4 bg-gray-200 rounded-xl border placeholder-gray-900','placeholder':'Enter your new topic here'})
        }
    def raise_exception_for_duplicate_topic(self):
        value = self.cleaned_data['topic']  

        # Check if the value already exists in the database
        if Community.objects.filter(topic=value).exists():
            raise forms.ValidationError('This value already exists. Please choose a different one.')

        return value
    
class MessageForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=('content',)
        widgets={
            'content':forms.Textarea(attrs={'class':'w-full bg-gray-200 px-6 py-4 rounded-xl border placeholder-gray-900','placeholder':'type your new message here'})
        }

    