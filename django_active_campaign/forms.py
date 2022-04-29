from django import forms
from integrations import Credential

class ActiveCampaignIntegrationForm(forms.ModelForm):

    class Meta:
        model = Credential
        fields = ['client_url', 'private_key']
        labels = {
            'client_url': _("Active Campaign URL"),
            'private_key': _("Active Campaign Key")
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_url'].required = True
        self.fields['private_key'].required = True