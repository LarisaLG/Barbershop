from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """This class generates a form from the Booking model
    """

    name = forms.CharField()

    email = forms.EmailField(widget=forms.TextInput(),)

    phone = forms.IntegerField(required=True, widget=forms.TextInput(),)

    date = forms.DateField(
        validators=[MinValueValidator(get_min_date)],
        widget=DateInput(attrs={'type': 'date', 'min': get_min_date}))

    class Meta:
        model = Booking
        fields = ('name', 'phone', 'service', 'date', 'time')
