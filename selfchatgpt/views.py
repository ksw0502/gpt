from django.shortcuts import render
import mlflow
import mlflow.keras
from chatgpt.views import chatGPT
# Create your views here.
import openai
openai.api_key = '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'

def index(req):
    return render(req, 'selfchatgpt/index.html')


def chatGPT(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print(completion)
    result = completion.choices[0].message.content
    return result


def chat(req):
    prompt = req.POST.get('question')
    
    result = chatGPT(prompt)
    context={
        'question':prompt,
        'result': result
    }
    
    return render(req, 'selfchatgpt/result.html',context)