from django.shortcuts import render
from django.http import HttpResponse

from .scraper import say_a_joke
#from .forms import UploadFileForm
from .csv_to_xls_writer import xlsx_writer
from django.utils.encoding import smart_str
from openpyxl.writer.excel import save_virtual_workbook

def home(request):
    return render(request, 'index.html')

def jokes(request):
    return render(request, 'jokes.html', {'rand_joke':say_a_joke()})


def bulls_and_cows(request):
    return HttpResponse('bulls_and_cows')

def csv_to_xlsx(request):
    if  request.method == 'POST':
        new_file = xlsx_writer(request.FILES)

        response = HttpResponse(content=save_virtual_workbook(new_file), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Perfect.xlsx'
        return response

    else:
        return render(request, 'csv_to_xlsx.html')# {'form': form})


def mercury_retrograde(request):
    return HttpResponse('mercury_retrograde')
