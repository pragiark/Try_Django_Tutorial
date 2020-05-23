from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-mame two",
                "id": "my-id-for-textarea",
                   "rows": 20,
                   "cols": 120

            }
        )
    )
    price = forms.DecimalField(initial=100.22)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "ARO" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-mame two",
                "id": "my-id-for-textarea",
                   "rows": 20,
                   "cols": 120

            }
        )
    )
    price = forms.DecimalField(initial=100.22)