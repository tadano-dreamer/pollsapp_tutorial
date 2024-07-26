from django.db.models import F 
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm # ユーザー作成のため追加
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.template import loader
from .forms import ChatForm
import openai

from .models import Choice, Question

@login_required
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

    

@login_required
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    chat_ans_header=""
    chat_results=""
    
    # ChatGPTボタン押下時
    if request.method == "POST":
        choice_set = []
        if question.choice_set.exists():  # この行を追加
            for choice in question.choice_set.all():
                choice_set.append([choice.choice_text])
        else:
            # 選択肢が存在しない場合の処理
            choice_set = "" 
        
        openai.api_key = "" #自身のAPIキーを入力
        prompt = "次のQuestionとChoiceを参考にして、質問（Question）に対する他の選択肢（Choice）を5つ提示してください。\n" + "Question:" + str(question) + "\n" + "Choice:" + str(choice_set)
        print("==(ChatGPTへのプロンプト)==\n",prompt,"\n====")

        # ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "日本語で応答してください。可能な限りシンプルに回答してください。"
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ],
        )

        chat_ans_header = 'ChatGPTによる他の選択肢の候補'
        chat_results = response.choices[0].message.content

    context = {
        "question": question,
        'chat_results': chat_results,
        'ans_header': chat_ans_header
    }
    return render(request, "polls/detail.html", context)



@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
            form = ChatForm()
            context={
                "question": question,
                "error_message": "ラジオボタンを選択してください",
                "form": form,
                }      
            return render(request,"polls/detail.html" ,context)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    

@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("polls:login"))
    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})


def addchoice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        question.choice_set.create(choice_text=request.POST.get('add'), votes=0)
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    
    else:
        return render(request, "polls/addchoice.html", {"question": question})