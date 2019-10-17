# coding=UTF-8

from django import forms

#from phonenumber_field.modelfields import PhoneNumberField
"""from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select

class PhoneWidget(MultiWidget):
    def __init__(self, code_length=3, num_length=7, attrs=None):
        widgets = [TextInput(attrs={'size': code_length, 'maxlength': code_length, "class":"mr-2"}),
                   TextInput(attrs={'size': num_length, 'maxlength': num_length})]
        super(PhoneWidget, self).__init__(widgets, attrs)

    def format_output(self, rendered_widgets):
        return '+7' + '(' + rendered_widgets[0] + ') - ' + rendered_widgets[1]

    def decompress(self, value):
        if value:
            return [value.code, value.number]
        else:
            return ['', '']


class PhoneField(MultiValueField):
    def __init__(self, code_length, num_length, *args, **kwargs):
        list_fields = [CharField(),
                       CharField()]
        super(PhoneField, self).__init__(list_fields, widget=PhoneWidget(code_length, num_length), *args, **kwargs)

    def compress(self, values):
        return '+7' + values[0] + values[1]  #Собственно, стандартизация строки номера эстетики ради

"""
class PaymentForm(forms.Form):
	FIO = forms.CharField(max_length=100)
	address = forms.CharField(max_length=100)
	#phone = PhoneNumberField()
