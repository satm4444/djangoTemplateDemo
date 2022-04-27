from django.shortcuts import render


# Create your views here.
def renderTemplate(request):
    myDict = {"name": "Satyam Rawal"}
    return render(request, 'templatesApp/firstTemplate.html', myDict)


def renderEmployee(request):
    empDic = {"id": 1, "name": "Satyam Rawal",
              "address": "Basundhara kathmandu"}
    return render(request, 'templatesApp/employeeTemplate.html', empDic)
