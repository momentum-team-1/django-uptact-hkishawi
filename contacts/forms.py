from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            # 'address_1',
            # 'address_2',
            # 'city',
            # 'state',
            # 'zip_code',
            'phone_number',
            'email',
            'company_name',
            'birthday',
            'note',
          
        ]   
class AddressForm(forms.ModelForm):
    class Meta: 
        model = Address
        fields = [
            'address_type',
            'line_1',
            'line_2',
            'city',
            'state',
            'zip_code',
        ]