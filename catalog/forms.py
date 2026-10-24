from django import forms
from django.core.exceptions import ValidationError

from .models import Product
from .validators import validate_no_forbidden_words


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'category':
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

        self.fields['name'].widget.attrs.update({'placeholder': 'Введите название'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Введите описание', 'rows': 4}
        )
        self.fields['price'].widget.attrs.update({'placeholder': 'Введите цену'})

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        validate_no_forbidden_words(name)
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        validate_no_forbidden_words(description)
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            self.add_error('price', 'Цена не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('Формат файла должен быть JPEG или PNG.')
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер файла не должен превышать 5 МБ.')
        return image
