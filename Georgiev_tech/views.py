### Shared
from django.shortcuts import render
from django.http import HttpResponse
### For the jokes module
from .scraper import say_a_joke
### For the csv to excel module
from .forms import UploadFileForm
from .csv_to_xls_writer import xlsx_writer
from openpyxl.writer.excel import save_virtual_workbook
from django.views.generic.edit import FormView


### Overriding the post method of FormView subclass to handle multiple file uploads
class FileFieldView(FormView):
    form_class = UploadFileForm
    template_name = 'csv_to_xlsx.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

### views
def home(request):
    return render(request, 'index.html')


def jokes(request):
    return render(request, 'jokes.html', {'rand_joke':say_a_joke()})


def bulls_and_cows(request):
    return HttpResponse('bulls_and_cows')


def csv_to_xlsx(request):
    if  request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = xlsx_writer(request.FILES)

        response = HttpResponse(content=save_virtual_workbook(new_file), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=Perfect.xlsx'
        return response
    else:
        form = UploadFileForm()
    return render(request, 'csv_to_xlsx.html', {'UploadFileForm':UploadFileForm})


def mercury_retrograde(request):
    return HttpResponse('mercury_retrograde')
