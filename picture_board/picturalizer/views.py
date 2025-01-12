from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from . import models
from .models import Image, Comment
from .forms import ImageForm, CommentForm


def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showall')
    else:
        form = ImageForm()

    context = {'form':form}
    return render(request, 'upload.html', context)

class ImageUploadView(CreateView):
    template_name = 'upload.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse_lazy('picturalizer:showall')
    


class CommentUploadView(CreateView):
    template_name = 'upload.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('showall')


class ShowAllView(ListView):
    model = Image
    template_name = 'show_all_thread.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data(**kwargs)
        print(ctxt)
        return ctxt
    

def thread(request, pk):
    model = Image.objects.get(id=pk)
    form = CommentForm()

    if request.method == "POST":
        print("POSTーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
        form = CommentForm(request.POST)

        if form.is_valid():
            print("validation成功ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー")
            text = form.cleaned_data['text']
            author = form.cleaned_data['author']
            comment = Comment(
                image=model, 
                text=text, 
                author=author)
            comment.save()

    else:
        form = CommentForm()

    return render(request, "thread.html", {
        "model": model,
        "form": form})

class ThreadView(DetailView, generic.edit.ModelFormMixin):
    model = Image
    template_name = 'thread.html'
    fields = ()

    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data(**kwargs)
        ctxt.update({
            'comment_form': CommentForm(**self.get_form_kwargs()),
        })
        return ctxt
    
    def post(self, request, *args, **kwargs):
        if 'button_change_question_text' in request.POST:
            qform = CommentForm(**self.get_form_kwargs())

            if qform.is_valid():
                qform_query = qform.save(commit=False)
                qform_query.pk = Image.objects.filter(pk=self.kwargs['pk'])
                qform_query.save()
                return self.form_valid(qform)
            else:
                self.object = self.get_object()
                return self.form_invalid(qform)