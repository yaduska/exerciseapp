from django.urls import path
from .views import fill_from,new_plan,existing_plans

app_name='plans'

urlpatterns = [
    path('fill/',fill_from,name='fillform'),
    path('new/',new_plan,name='newplan'),
    path('existingplan/',existing_plans,name='existingplan')
]
