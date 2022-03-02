from django.shortcuts import render,redirect
from .forms import TrainerForm
from .models import Trainer


def trainer_list(request):
    context = {'trainer_list':Trainer.objects.all()}
    return render(request, 'crud_trainer/trainer_list.html',context)

def register_trainer(request,id=0):
    if request.method == "GET":
        if id==0:
            form = TrainerForm()
        else:
            trainer = Trainer.objects.get(pk=id)
            form = TrainerForm(instance=trainer)
        return render(request, 'crud_trainer/register_trainer.html',{'form':form})
    else:
        if id==0:
            form = TrainerForm(request.POST)
        else:
            trainer = Trainer.objects.get(pk=id)
            form = TrainerForm(request.POST,instance=trainer)
        if form.is_valid():
            form.save()
        return redirect('/list')

def trainer_delete(request,id):
    trainer = Trainer.objects.get(pk=id)
    trainer.delete()
    return redirect('/list')
