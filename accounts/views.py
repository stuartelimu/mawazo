from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import View
from django.urls import reverse_lazy
from blog.models import Author
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate

User = get_user_model()


class SignUpView(View):
    form_class = UserCreationForm
    # success_url = reverse_lazy("login")
    template_name = "signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            author = User.objects.get(username=user)
            Author.objects.create(user=author)
            login(request, user)
            return redirect(reverse_lazy("blog:index"))
        return render(request, self.template_name, {'form':form})
