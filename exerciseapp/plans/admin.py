from django.contrib import admin

from .models import UserDetails,DietPlan,ExercisePlan,Plans

# Register your models here.
admin.site.register(UserDetails)
admin.site.register(DietPlan)
admin.site.register(ExercisePlan)
admin.site.register(Plans)
