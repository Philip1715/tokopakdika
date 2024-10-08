from django.forms import ModelForm
from main.models import ProductEntry
from django.utils.html import strip_tags
class ProductForm(ModelForm):
    class Meta:
        model = ProductEntry
        fields = ["name", "description", "price", "stock"]

    def clean_prodcut(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_feelings(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
