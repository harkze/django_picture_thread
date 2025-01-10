from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse
from django.http import Http404

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

class UploadView(CreateView):
    template_name = 'picturalizer/upload.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse('picturalizer:showall')



def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'picturalizer/show_all_thread.html', context)

class ShowAllView(ListView):
    model = Image
    template_name = 'picturalizer/show_all_thread.html'



def thread(request, image_id):
    images = Image.objects.all()[0]
    context = {'images':images}
    return render(request, '', context)

class ThreadView(DetailView):
    model = Image
    template_name = 'picturalizer/thread.html'

    # def get_context_data(self, **kwargs):
    #     print("*"*200)
    #     for i in self.request:
    #         print(i)
    #     print("*"*200)
    #     context = super().get_context_data(**kwargs)
    #     comment = Comment.objects.filter(image=self.request.POST["pk"])
    #     context['comments'] = comment  # コメントを取得
    #     return context