from django import forms
from . import models 

class GoodForm(forms.ModelForm):
    matrix = forms.CharField(label='Матриця', required=False)
    CPU = forms.CharField(label='Процесор', required=False)
    GPU = forms.CharField(label='Відеокарта', required=False)
    RAM = forms.CharField(label='Оперативна пам\'ять', required=False)
    SSD = forms.CharField(label='Накопичувач', required=False)
    
    class Meta:
        model = models.Good
        fields = ['title', 'description', 'price', 'manufacturer', 'main_picture']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Заполняем начальные значения из JSONField
        if self.instance.pk and self.instance.characteristics:
            for key in ['matrix', 'CPU', 'GPU', 'RAM', 'SSD']:
                if key in self.fields:
                    self.fields[key].initial = self.instance.characteristics.get(key, '')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Сохраняем значения обратно в JSONField
        instance.characteristics = {
            'matrix': self.cleaned_data.get('matrix', '0'),
            'CPU': self.cleaned_data.get('CPU', ''),
            'GPU': self.cleaned_data.get('GPU', ''),
            'RAM': self.cleaned_data.get('RAM', '0GB'),
            'SSD': self.cleaned_data.get('SSD', '0GB'),
        }
        if commit:
            instance.save()
        return instance
