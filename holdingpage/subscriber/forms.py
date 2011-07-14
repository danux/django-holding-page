from django import forms
from holdingpage.subscriber.models import Subscriber

class SubscriberForm(forms.ModelForm):
    
    class Meta():
        model = Subscriber
        fields = ['full_name', 'email', 'source_share_code']
        widgets = {
            'source_share_code': forms.HiddenInput(),
        }
        
    def clean_source_share_code(self):
        if self.cleaned_data['source_share_code'] != '':
            try:
                Subscriber.objects.get(share_code=self.cleaned_data['source_share_code'])
            except:
                raise forms.ValidationError('Invalid share code.')
        return self.cleaned_data['source_share_code']