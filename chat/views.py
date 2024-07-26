from django.http import HttpResponse
from django.template import loader
from .forms import ChatForm
import openai

# Create your views here.


def index(request):
    """
    チャット画面
    """

    # 応答結果
    chat_results = ""

    if request.method == "POST":
        # ChatGPTボタン押下時

        form = ChatForm(request.POST)
        if form.is_valid():

            sentence = form.cleaned_data['sentence']

            # TODO: APIキーのハードコーディングは避ける
            openai.api_key = "" # 自身のAPIキーを入力

            # ChatGPT
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "日本語で応答してください"
                    },
                    {
                        "role": "user",
                        "content": sentence
                    },
                ],
            )

            chat_results = response["choices"][0]["message"]["content"]

    else:
        form = ChatForm()

    template = loader.get_template('chat/index.html')
    context = {
        'form': form,
        'chat_results': chat_results
    }
    return HttpResponse(template.render(context, request))
