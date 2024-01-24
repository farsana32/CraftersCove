from django import forms
from django.core.validators import MinLengthValidator
from .models import Account


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100, validators=[MinLengthValidator(4,"4 or more characters needed")])
    last_name = forms.CharField(label='Last Name', max_length=100, validators=[MinLengthValidator(4)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'confirm Password'
    }))
    class Meta:
        model = Account
        fields =['first_name','last_name','phone_number','email','password']


    def clean(self):
        cleaned_data=super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password !=confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter first Name' 
        self.fields['last_name'].widget.attrs['placeholder']='Enter last Name' 
        self.fields['phone_number'].widget.attrs['placeholder']='Enter phone Number' 
        self.fields['email'].widget.attrs['placeholder']='Enter Email Address' 
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control' 



