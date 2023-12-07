from django import forms

from .models import UserDetails 

CLASS_ATTR='w-full px-6 py-4 rounded-xl border'
class UserDetailForm(forms.ModelForm):
    
    class Meta:
        model = UserDetails
        fields = ('gender','age','height','weight','workout_time','preferred_workout_time',)
        widgets={
            'gender':forms.Select(attrs={'class':CLASS_ATTR,'placeholder':'Enter your gender'}),
            'age':forms.NumberInput(attrs={'class':CLASS_ATTR,'placeholder':'Enter your age'}),
            'height':forms.NumberInput(attrs={'class':CLASS_ATTR,'placeholder':'Enter your height in cm'}),
            'weight':forms.NumberInput(attrs={'class':CLASS_ATTR,'placeholder':'Enter your weight in kg'}),
            'workout_time':forms.Select(attrs={'class':CLASS_ATTR,'placeholder':'Enter your workout time '}),
            'preferred_workout_time':forms.Select(attrs={'class':CLASS_ATTR,'placeholder':'Enter your preferred workout time'}),
        }
    