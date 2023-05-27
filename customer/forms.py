from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder':'Username',
             'name':"username",
             'type':"text", 
             'class':"form-control" ,
             'autocomplete':"on",
             'aria-label':"Username"
        })
        self.fields['email'].widget.attrs.update({
            'placeholder':'Email Address',
             'name':"email",
             'type':"email", 
             'class':"form-control" ,
             'autocomplete':"on",
             'aria-label':"Email Address"
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder':'Password',
             'name':"password1",
             'type':"password", 
             'class':"form-control" ,
             'autocomplete':"off",
             'aria-label':"Password"
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder':'Confirm Password',
             'name':"password1",
             'type':"password", 
             'class':"form-control" ,
             'autocomplete':"off",
             'aria-label':"Password"
        })
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']