from django import forms


class UppercaseCharField(forms.CharField):
    def clean(self, value):
        value = super().clean(value)
        if value:
            value = value.title()
        return value

class FormReservas(forms.Form):
    nombre = UppercaseCharField(max_length=50 , widget=forms.TextInput(attrs={'class': 'form-control','id': 'labelInput'}))
    apellido = UppercaseCharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','id': 'labelInput'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','id': 'labelInput'}))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type': 'date', 'id': 'labelInput'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control','type': 'time', 'id': 'labelInput'}))
    personas = forms.IntegerField( widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'labelInput'}))
    comentarios = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40,'class': 'form-control','id': 'labelInput'}))
