from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead, User
from django.core.exceptions import ValidationError

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'image']


    def clean_name(self):    
        data = self.cleaned_data['name']
        if "lead" not in data:
            raise ValidationError("Name has to include Lead")
        return data   

       


class NewForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','email', 'username', 'is_organiser' , 'is_agent']
        fields_class = {"username" : UsernameField}
        labels = {'is_organiser': 'Organiser', 'is_agent': 'Agent'}



    def __init__(self, *args, **kwargs):
        super(NewForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
