from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from pip._internal.utils import logging
from .models import BP


# Create your views here.

def post_list(request):

    posts = BP.objects.all() #(date__lte=timezone.now)
    return render(request, 'calculator/post_list.html', {'posts': posts})

# This view will be responsible to read the excel file https://www.pythoncircle.com/post/591/how-to-upload-and-process-the-excel-file-in-django/




def index(request):
    data = {}
    if "GET" == request.method:
        return render(request, 'calculator/index.html', {})

    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("myapp_calc:index"))
        #if file is too large, return
        if csv_file.multiple_chunks():
            messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            return HttpResponseRedirect(reverse("myapp_calc:index"))

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split('\n')
        #loop over the lines and save them in db. If error , store as string and then display
        for line in lines:
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["start_date_time"] = fields[1]
            data_dict["end_date_time"] = fields[2]
            data_dict["notes"] = fields[3]
            try:
                form = EventsForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    logging.getLogger("error_logger").error(form.errors.as_json())
            except Exception as e:
                logging.getLogger("error_logger").error(repr(e))
                pass

    except Exception as e:
        logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
        messages.error(request,"Unable to upload file. "+repr(e))

    return HttpResponseRedirect(reverse("myapp_calc:index"))
    # else:
    #     excel_file = request.FILES["excel_file"]
    # 
    #     wb = openpyxl.load_workbook(excel_file)
    # 
    #     # getting a particular sheet by name out of many sheets
    #     worksheet = wb["Sheet1"]
    #     print(worksheet)
    # 
    #     excel_data = list()
    #     # iterating over the rows and
    #     # getting value from each cell in row
    #     for row in worksheet.iter_rows():
    #         row_data = list()
    #         for cell in row:
    #             row_data.append(str(cell.value))
    #         excel_data.append(row_data)
    # 
    #     return render(request, 'calculator/index.html', {"excel_data": excel_data})
