from django.shortcuts import render, redirect
from .models import Image, Comment
from .forms import ImageForm


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('picturalizer:showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'picturalizer/upload.html', context)

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'picturalizer/show_all_thread.html', context)


def thread(request, image_id):
    images = Image.objects.all()[0]
    context = {'images':images}
    return render(request, 'picturalizer/thread.html', context)
