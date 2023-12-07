from django.shortcuts import render,redirect,get_object_or_404
from .models import Community,Message
from .forms import CommunityForm,MessageForm
from django.contrib.auth.decorators import login_required


def show_all(request):
    user_topics= Community.objects.filter(users__in=[request.user.id]).exclude(topic='review app')
    other_topics=Community.objects.exclude (users__in=[request.user.id]).exclude(topic='review app')
    community = Community.objects.filter(topic='review app').first()
    return render(request,'community/comhome.html',{'user_topics':user_topics,'other_topics':other_topics,'community':community}) 

@login_required
def show_message(request,community_pk):
    community= get_object_or_404(Community,pk=community_pk)
    messages=Message.objects.filter(community=community)
    if request.method== 'POST':
        form=MessageForm(request.POST)
        if form.is_valid():
            message= form.save(commit=False)
            message.community=community
            message.created_by=request.user
            message.save()
    else:
        form=MessageForm()
        
    return render(request,'community/showmessage.html',{'form':form,'community':community,'messages':messages})

@login_required
def new_community(request):
    if request.method == 'POST':
        community_form = CommunityForm(request.POST)
        message_form = MessageForm(request.POST)
        if community_form.is_valid():
            community = community_form.save()
            community.users.add(request.user)
            community.save()
            
            message_form = MessageForm(request.POST)
            if message_form.is_valid():
                message = message_form.save(commit=False)
                message.community = community
                message.created_by = request.user
                message.save()
        
            
            else:
               message_form = MessageForm() 
        return redirect('community:showmessage', community_pk=community.id) 
    else:
        community_form= CommunityForm()
        message_form = MessageForm() 

             
        
                #return redirect('community:showmessage', community_pk=community.id)

    return render(request, 'community/newcommunity.html', {'community_form': community_form,'message_form':message_form})

def new_review(request):
    community = Community.objects.filter(topic='review app').first()
    message_form =MessageForm(request.POST)    
    if message_form.is_valid():
        message= message_form.save(commit=False)
        message.community=community
        message.created_by=request.user
        message.save()
        return redirect('community:reviewall')
    else:
        message_form=MessageForm()
    return render(request,'community/newreviewapp.html',{'message_form':message_form})

def review_all(request):
      already_commented=False
      community = Community.objects.filter(topic='review app').first()
      messages= Message.objects.filter(community=community)
      return render(request,'community/reviewapp.html',{'messages':messages,'already_commented':already_commented})         
        


