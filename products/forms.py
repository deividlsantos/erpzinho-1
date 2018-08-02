from django import forms
from .models import Product
from ckeditor.widgets import CKEditorWidget

class ProductForm(forms.ModelForm):

    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'