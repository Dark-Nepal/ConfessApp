from django.shortcuts import render
from confess.forms import ConfessForm
from datetime import datetime


def home(request):
    if request.method == 'POST':
        filled_form = ConfessForm(request.POST)
        if filled_form.is_valid():
            filled_form.post_date = datetime.now()
            icon = True
            note = 'Your confession is sent !'
            filled_form.save()
            newform = ConfessForm()
            return render(request, 'index.html', { 'form':newform, 'icon': icon, 'note':note })

        """
           Store the confession and show the message
           3:18 PM 8/12/22 by Deepesh Mahato
        """
    else:
        form = ConfessForm()
        return render(request, 'index.html',{ 'form':form, })

    
