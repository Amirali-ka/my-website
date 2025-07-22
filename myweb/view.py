from django.shortcuts import render
def index_view(request):
    manual_info={'name':'amirali','lastname':'kavoossi'
                 ,'email':'kavoossi1co@gmail.com','facebook':'https://www.facebook.com/share/16aV98AZ5U/'
                   ,'github':'https://github.com/Amirali-ka','linkedin':'http://www.linkedin.com/in/amirali-kavoossi'}
    return render(request,'index.html',manual_info)