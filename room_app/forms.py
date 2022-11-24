from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Booking


class PostForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

# class DateForm(forms.Form):
#     date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])