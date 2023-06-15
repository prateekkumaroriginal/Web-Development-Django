from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

punctuation_symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]


def index(request):
    return render(request, "index.html")


def analyze(request):
    text = request.POST.get('raw_text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    capfirst = request.POST.get('capfirst', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    if removepunc == "on":
        text = text.lower()
        for ch in punctuation_symbols:
            text = text.replace(ch, '')

    if fullcaps == "on":
        text = text.upper()
    elif capfirst == "on":
        text = text.title()

    if newlineremove == "on":
        text = text.replace('\n', ' ')
        text = text.replace('\r', ' ')

    if extraspace == "on":
        while '  ' in text:
            text = text.replace('  ', ' ')

    char_count = len(text)
    word_count = len([word for word in text.split()
                     if word not in punctuation_symbols])

    return render(request, "analyze.html", {
        'analyzed_text': text,
        'char_count': char_count,
        'word_count': word_count,
    })
