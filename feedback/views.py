from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
def smth(request):
    return render(request, 'feedback.html', {})

def feedback(request):
    if request.POST:
        form = ContactForm(request.POST)
        # Если форма прошла валидацию
        if form.is_valid():
            cd = form.cleaned_data
            # ... сохранение в базу, к примеру
            # здесь мы просто выведем результат на экран
            smth(request)
            #return HttpResponse(
                #'Name: %s, Email: %s, Message: %s' %
                #(cd['name'], cd['email'], cd['message'])
            #)
    else:
        form = ContactForm()
    return render(request, 'feedback.html', {'form': form})
