from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

punctuation_symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]


def index(request):
    return render(request, "index.html")


def analyze(request):
    text = request.GET.get('raw_text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capfirst = request.GET.get('capfirst', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    extraspace = request.GET.get('extraspace', 'off')

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
