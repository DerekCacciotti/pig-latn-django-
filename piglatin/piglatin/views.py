from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse(render(request, 'home.html'))

def translate(request):
    
    usertext = request.GET['enteredtext'].lower()
    piglatin = ''

    for word in usertext.split():
      if word[0] in ['a', 'e', 'i', 'o' 'u']:
          piglatin += word
          piglatin += ' yay '
      else:
         piglatin += word[1:]
         piglatin += word[0]
         piglatin += ' ay '



    return render(request, 'translate.html', {'text': usertext, 'piglatin': piglatin})




def about(request):
   return HttpResponse(render(request, 'about.html'))

   