from django.shortcuts import render
from django.http import HttpResponse
from formz import cian_parser_lvl2
from formz import magic
from .forms import NameForm
import mimetypes
import os
import urllib

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cd = form.cleaned_data
            cian_parser_lvl2.main(int(cd['you1ame']))
            title_ = cian_parser_lvl2.title
            #title_='ЖК «Кленовые Аллеи»'
            #URLEncodedFileName = urllib.parse.urlencode([('', title_)], encoding="UTF-8")
           # URLEncodedFileName = URLEncodedFileName.replace('=','')
           # title_ = URLEncodedFileName.replace('+',' ')
            file_=title_+'.csv'
            path = os.path.abspath(file_)
            data = open(path, "rb").read()
            response = HttpResponse(data, content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="%s"' %(file_)
            #response['Content-Disposition'] = 'attachment; filename="sss"; filename*=UTF-8''%s'%(file_)
            return response


            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/thanks/')
            #return render(request, 'formz/my_formz.html', {'form': form})
            #return HttpResponse('Скачен ЖК с ID: %d' % int(cd['you1ame']))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'formz/my_formz.html', {'form': form})

