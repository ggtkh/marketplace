from django import forms
from . import models 

class GoodEditForm(forms.ModelForm):
    class Meta:
        model = models.Good
        fields = ['title', 'description', 'price', 'manufacturer', 'main_picture',
                  'screen_diagonal', 'screen_refresh_rate', 'CPU', 'GPU', 'RAM', 
                  'storage_capacity']
        
        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'price': 'Ціна',
            'manufacturer': 'Виробник',
            'main_picture': 'Головне зображення',
            'screen_diagonal': 'Діагональ екрану',
            'screen_refresh_rate': 'Частота оновлення екрану',
            'CPU': 'Процесор',
            'GPU': 'Відеокарта',
            'RAM': 'Оперативна пам\'ять',
            'storage_capacity': 'Накопичувач',
        }

        help_texts = {
            'screen_diagonal': '" Наприклад: 15.6(")',
            'screen_refresh_rate': 'Наприклад: 144Hz',
            'price': '₴',
            'RAM': 'Наприклад: 16GB',
            'storage_capacity': 'Наприклад: 512GB',
        }


class GoodCreateForm(forms.ModelForm):
    class Meta:
        model = models.Good
        fields = ['title', 'description', 'price', 'manufacturer', 'main_picture', 
                  'is_available', 'screen_diagonal', 'screen_refresh_rate', 
                  'CPU', 'GPU', 'RAM', 'storage_capacity']
        
        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'price': 'Ціна',
            'manufacturer': 'Виробник',
            'main_picture': 'Головне зображення',
            'is_available': 'В наявності',
            'screen_diagonal': 'Діагональ екрану',
            'screen_refresh_rate': 'Частота оновлення екрану',
            'CPU': 'Процесор',
            'GPU': 'Відеокарта',
            'RAM': 'Оперативна пам\'ять',
            'storage_capacity': 'Накопичувач',
        }

        help_texts = {
            'screen_diagonal': '" Наприклад: 15.6(")',
            'screen_refresh_rate': 'Наприклад: 144Hz',
            'price': '₴',
            'RAM': 'Наприклад: 16GB',
            'storage_capacity': 'Наприклад: 512GB',
        }