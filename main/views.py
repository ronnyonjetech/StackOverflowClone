from django.shortcuts import render
from .models import Question,Answer,Comment
from django.core.paginator import Paginator

# Create your views here.
def main(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.filter(title__icontains = q).order_by('-id')
    else:
        quests=Question.objects.all().order_by('-id')
        
    paginator=Paginator(quests,2)
    page_num=request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'home.html',{'quest':quests})

def detail(request,id):
    quests=Question.objects.get(pk=id)
    tags=quests.tags.split(',')
    answer=Answer.objects.get(question=quests)
    comments=Comment.objects.filter(answer=answer).order_by('-id')
    return render(request,'detail.html',{
        'quest':quests,
        'tags':tags,
        'answer':answer,
        'comments':comments
        })