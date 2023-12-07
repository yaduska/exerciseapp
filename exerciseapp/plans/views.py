from django.shortcuts import render,redirect
from .forms import UserDetailForm
from .models import Plans, UserDetails,DietPlan,ExercisePlan
from django.contrib.auth.decorators import login_required

@login_required
def fill_from(request):
    user_detail_object = UserDetails.objects.filter(user=request.user).first()
    if user_detail_object and  user_detail_object.user_detail.exists():
        return redirect('plans:existingplan')
    else:
        if request.method=='POST':
            form=UserDetailForm(request.POST) 
            if form.is_valid():
                user_detail=form.save(commit=False)
                user_detail.user=request.user
                user_detail.save()
            return redirect('plans:newplan')
        else:
            form=UserDetailForm()
        
    
    return render(request,'plans/userdetailforms.html',{'form':form})

@login_required
def new_plan(request):
    exerciseplan = ''
    dietplan = ''

    user_detail_object = UserDetails.objects.filter(user=request.user).first()
    if user_detail_object and user_detail_object.user_detail.exists():
         return redirect('plans:existingplan')
    if user_detail_object and (not user_detail_object.user_detail.exists()):
        height = user_detail_object.height
        weight = user_detail_object.weight
        age = user_detail_object.age
        #workout_time = user_detail_object.workout_time
        preferred_workout_time = user_detail_object.preferred_workout_time

        bmi = weight / ((height / 100) ** 2)

        if 15 < age < 60: 
            if bmi>25:
                dietplan = DietPlan.objects.filter(name='heavydiet').first()
                if preferred_workout_time == 'morning':
                    exerciseplan = ExercisePlan.objects.filter(name='moremorning').first()
                  
                else:
                    exerciseplan = ExercisePlan.objects.filter(name='moreevening').first()
               
            elif bmi < 18.5:
               dietplan = DietPlan.objects.filter(name='richdiet').first()
               if preferred_workout_time == 'morning':
                    exerciseplan = ExercisePlan.objects.filter(name='lessmorning').first()
                        
               else:
                    exerciseplan = ExercisePlan.objects.filter(name='lessevening').first()

                
            elif 18.5 <= bmi <= 25:
                dietplan =DietPlan.objects.filter(name='milddiet').first()
                if preferred_workout_time == 'morning':
                    exerciseplan = ExercisePlan.objects.filter(name='moderatemorning').first()
                        
                else:
                    exerciseplan = ExercisePlan.objects.filter(name='moderateevening').first()



        elif age > 60:
            exerciseplan = ExercisePlan.objects.filter(name='runwalk').first()
            dietplan = DietPlan.objects.filter(name='Dietplanforelderpeople').first()
        else:
            exerciseplan = 'none'
            dietplan='none'
    plan= Plans.objects.create(
        name=request.user.username+'_plan',
        user_details=user_detail_object,
        description=request.user.username+'_plan with '+dietplan.name+exerciseplan.name,
        diet_plan=dietplan,
        exercise_plan=exerciseplan)
    
    
    return render(request, 'plans/plans.html', {'exerciseplan': exerciseplan, 'dietplan': dietplan,'user_detail_object':user_detail_object})
    
@login_required
def existing_plans(request):
    user_detail_object = UserDetails.objects.filter(user=request.user).first()
    return render (request,'plans/existingplans.html',{'exerciseplan': user_detail_object.user_detail.first().exercise_plan, 'dietplan': user_detail_object.user_detail.first().diet_plan,'user_detail_object':user_detail_object})