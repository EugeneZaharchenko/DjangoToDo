from django.shortcuts import render, redirect

from .models import Task


def main(request):
    tasks = Task.objects.all()[:7]
    context = {
        "tasks": tasks
    }
    return render(request, 'main.html', context)


def details(request, x):
    exact_task = Task.objects.get(id=x)
    context = {
        "todo": exact_task
    }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['details']
        task = Task(title=title, details=text)
        task.save()
        return redirect('main')
    else:
        return render(request, 'add.html')


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('main')


def check(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('main')


def uncheck(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('main')
