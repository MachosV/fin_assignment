from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
# Create your views here.

class LoginTemplate(generic.TemplateView):
    template_name="finloup/login.html"
    
    def post(self, request, **kwargs):
        qd = request.POST
        if qd.__contains__("password") and qd.__contains__("username"):
            username = qd["username"]
            password = qd["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect("TestTemplate")
        return super(LoginTemplate,self).render_to_response({"message":"Invalid username/password"})


class TestTemplate(LoginRequiredMixin,generic.TemplateView):    

    login_url="LoginTemplate"
    
    template_name = 'finloup/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestTemplate, self).get_context_data(**kwargs)
        context["username"] = self.request.user
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data()
        qd = request.POST
        if qd.__contains__("budget"):
            context["message"] = "Invalid data"
            if qd["budget"].isnumeric():
                context["message"] = placeholderFunction(int(request.POST["budget"]))
        del qd
        return super(TestTemplate,self).render_to_response(context)

class LogoutView(generic.View):
    def post(self, request, **kwargs):
        logout(request)
        return redirect("LoginTemplate")

def placeholderFunction(data):
    return data+1