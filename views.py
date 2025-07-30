from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Questions
from .models import Choice
from django.urls import reverse
from django.template import loader

def index (request):
    latest_ques_list=Questions.objects.order_by('publ_time')[0:5]
    template=loader.get_template("polls/index.html")
    context={
        'latest_ques_list':latest_ques_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, question_id):
    try:
        question=Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist :
        raise Http404("Question is does not exist in database")
    return render(request, "polls/detail.html", {"question": question})

def result(request,question_id):
    question=get_object_or_404(Questions,pk=question_id)
    return render(request,"polls/result.html",{"question": question})

def vote(request , question_id):
    
    print(f"Vote view called with method: {request.method}")
    print(f"POST data: {request.POST}")
    # ... rest of your code
    #return HttpResponse("your looking at votes"%question_id)
    question=get_object_or_404(Questions,pk=question_id )
    try:
        
        selected_choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=selected_choice_id)
        #selected_choice=question.choice_set.get(pk=request.POST["Choice"])
        

        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:result",args=(question_id)))
        #return HttpResponse(template.render(context,request))
    #except:
        #return render(request,"polls/result.html",{"question":question,"error_message":"request is not valid"})
    
    except KeyError:
        return render(request, "polls/result.html", {
        "question": question,
        "error_message": "You didn't select a choice.",
        })
    except Choice.DoesNotExist:
        return render(request, "polls/result.html", {
        "question": question,
        "error_message": "Selected choice does not exist.",
        })

    
    


