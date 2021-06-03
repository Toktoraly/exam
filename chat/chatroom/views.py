from django.shortcuts import render
from .models import Massage
from .forms import MassageForm

# Create your views here.

def chatroom(request):
    massages = Massage.objects.all()
    form = MassageForm
    if request.method == "POST":
        form = MassageForm(request.POST)
        if form.is_valid():
            form.save

    return render(request, "chatroom/chatroom.html",{"massages":massages,"form":form})
