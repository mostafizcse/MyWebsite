from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, HttpResponseRedirect, render_to_response
from django.views.generic import TemplateView
from .models import author, category, article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import ContactForm, CreateForm, CreateFormMenu, CreateEmailForm, registerUser, requermentForm, sliderForm, reviewlistForm, eventForm, teamForm, featurlistForm
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
import threading

# Create your views here.

from .models import Logo, Team, Reviewlist, slider, Featurelist, Featuretitle, Reviewstitle, Post, Events, Requirments, Create_menu, Example, TeamTital, About_us, Address, Contact
def index(request):
    logo=Logo.objects.all()
    team=Team.objects.all()
    reviewtitle = Reviewstitle.objects.all()
    reviews=Reviewlist.objects.all()
    sliderlist=slider.objects.all()
    featurename=Featuretitle.objects.all()
    featurrlist=Featurelist.objects.all()
    mymanue=Create_menu.objects.all()
    teamtital=TeamTital.objects.all()
    poost=Post.objects.all()
    aboutus=About_us.objects.all()
    address=Address.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=id
        instance.save()

    yourform = CreateEmailForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.post=id
        instance.save()

    context = {
        'logo': logo,
        'team': team,
        'reviews': reviews,
        'sliderlist':sliderlist,
        'reviewtitle': reviewtitle,
        'featurrlist':featurrlist,
        'featurename':featurename,
        'form': form,
        'mymanue': mymanue,
        'teamtital':teamtital,
        'poost': poost,
        'aboutus': aboutus,
        'yourform': yourform,
        'address': address


    }
    return render(request, 'index.html', context)

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('create')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('create')
            else:
                return render(request, "login.html")
    return render(request, "login.html")


def getlogout(request):
    #return render(request, "login.html")
    logout(request)
    return redirect('login')

class emailThread(threading.Thread):
    html_content='contact.html'
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list)
        msg.content_subtype = "contact.html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    emailThread(subject, html_content, recipient_list).start()



def contact_view(request):
    address = Address.objects.all()
    form = ContactForm(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        to_subject = [save_it.subject]
        mymassage = 'thrding'
        form_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        threading.Thread(to_subject, mymassage,form_email,to_list)

        #def __init__(self, to_subject, mymassage,form_email,to_list):
         #   self.to_subject = [save_it.subject]
          #  self.mymassage = 'thrding'
           # self.form_email = 'mostafizcse1@gmail.com'
            #self.to_list = [save_it.email, settings.EMAIL_HOST_USER]
            #threading.Thread.__init__(self)

        #def run(self):
         #   msg = EmailMessage(self.to_subject, self.mymassage, self.form_email, self.to_list)
          #  msg.content_subtype = "html"
           # msg.send()

        send_mail(to_subject,mymassage,'mostafizcse1@gmail.com',to_list, fail_silently=False)
        threading(to_subject, mymassage,'mostafizcse1@gmail.com',to_list).start()
        return HttpResponseRedirect('/contact')
    return render(request, 'contact.html',{"form":form})


def emerging_tecnologies(request):
     poost=Post.objects.all()
     context={'poost':poost}
     return render(request, 'privacy-policy.html', context)


def post_details(request, post_id):
    post_details = Post.objects.get(pk=post_id)
    context = {'post_details': post_details}
    return render(request, 'privacy-policy-details.html', context)

def get_event(request):
    fullevent=Events.objects.all()
    context={'fullevent':fullevent}
    return render(request, 'event.html', context)


def getcreate(request):
    poost = Post.objects.all()
    form = CreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save();
        return redirect('emerging_tecnologies')
    return render(request, 'create.html',{"form":form,"poost":poost })

def getcreateUpdate(request, pid):
    data = get_object_or_404(Post, id=pid)
    form = CreateForm(request.POST or None, instance=data)
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save();
        return redirect('emerging_tecnologies')
    return render(request, 'create.html', {"form": form})

def getcreateDelete(request, pid):
    data=get_object_or_404(Post, id=pid)
    data.delete()
    return redirect('create')

def getcarear(request):
    myrequirment = Requirments.objects.all()
    context = {'myrequirment':myrequirment}
    return render(request, 'careers.html',context)

def cariar_details(request, cariar_id):
    cariar_details = Requirments.objects.get(pk=cariar_id)
    context = {'cariar_details':cariar_details}
    return render(request, 'careers-details.html', context)

def requirments_Create(request):
    myrequirment = Requirments.objects.all()
    myfrom = requermentForm(request.POST or None)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('careers')
    return render(request, 'requarment-create.html', {"myfrom": myfrom, "myrequirment":myrequirment})


def getRequermerntUpdate(request, pid):
    date=get_object_or_404(Requirments, id=pid)
    myfrom = requermentForm(request.POST or None,instance=date)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('careers')
    return render(request, 'requarment-create.html', {"myfrom": myfrom})

def getrequermerntDelete(request, pid):
    date=get_object_or_404(Requirments, id=pid)
    date.delete()
    return redirect('requermentCreate')



def slider_Create(request):
    sliderlist = slider.objects.all()
    myfrom = sliderForm(request.POST or None, request.FILES or None)
    if myfrom.is_valid():
        instance=myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'slider-create.html', {"myfrom": myfrom, 'sliderlist':sliderlist,})


def getsliderUpdate(request, pid):
    post=get_object_or_404(slider, id=pid)
    myfrom = sliderForm(request.POST or None, request.FILES or None, instance=post)
    if myfrom.is_valid():
        instance=myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'slider-create.html', {"myfrom": myfrom})

def getsliderDelete(request, pid):
    post=get_object_or_404(slider, id=pid)
    post.delete()
    return redirect('sliderCreate')

def reviewlist_Create(request):
    reviews=Reviewlist.objects.all()
    myfrom = reviewlistForm(request.POST or None)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'reviewlist-create.html', {"myfrom": myfrom, "reviews":reviews})

def getreviewlistUpdate(request, pid):
    data=get_object_or_404(Reviewlist, id=pid)
    myfrom = reviewlistForm(request.POST or None, instance=data)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'reviewlist-create.html', {"myfrom":myfrom})

def getreviewlistDelete(request, pid):
    data=get_object_or_404(Reviewlist, id=pid)
    data.delete()
    return redirect('reviewlistCreate')

def event_Create(request):
    fullevent = Events.objects.all()
    myfrom = eventForm(request.POST or None)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('event')
    return render(request, 'event-create.html', {"myfrom": myfrom, "fullevent": fullevent})

def getUpdate(request, pid):
    post=get_object_or_404(Events, id=pid)
    myfrom = eventForm(request.POST or None, instance=post)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('event')
    return render(request, 'event-create.html', {"myfrom": myfrom})


def getDelete(request, pid):
    post=get_object_or_404(Events, id=pid)
    post.delete()
    return redirect('eventCreate')

def add_menu(request):
    mymanue = Create_menu.objects.all()
    abcdef =Example.objects.all()
    context = {'mymanue':mymanue,'abcdef':abcdef}
    return render(request,'index2.html',context)


def menu_details(request, menu_id):
    menu_details = Create_menu.objects.get(pk=menu_id)
    context = {'menu_details':menu_details}
    return render(request, 'manu_page.html',context)
#getmanuUpdate
def getmenucreate(request):
    mymanue = Create_menu.objects.all()
    myfrom = CreateFormMenu(request.POST or None)
    if myfrom.is_valid():
        instance=myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'create_manu.html',{"myfrom":myfrom,"mymanue":mymanue})

def getmanuUpdate(request, pid):
    data=get_object_or_404(Create_menu, id=pid)
    myfrom = CreateFormMenu(request.POST or None, instance=data)
    if myfrom.is_valid():
        instance=myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'create_manu.html',{"myfrom":myfrom})

def getmanuDelete(request, pid):
    data=get_object_or_404(Create_menu, id=pid)
    data.delete()
    return redirect('menucreate')


def getRegister(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('login')
    return render(request, 'register.html', {"form": form})


def getbasehtml(request):
    return render(request, 'register.html')


def getadmin(request):
    return render(request, 'charts.html')


def team_create(request):
    team = Team.objects.all()
    myfrom = teamForm(request.POST or None, request.FILES or None)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'team-create.html', {"myfrom": myfrom,"team":team})


def getteamlistUpdate(request,pid):
    data=get_object_or_404(Team,id=pid)
    myfrom = teamForm(request.POST or None, request.FILES or None,instance=data)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'team-create.html', {"myfrom": myfrom})


def getteamlistDelete(request,pid):
    data=get_object_or_404(Team,id=pid)
    data.delete()
    return redirect('teamCreate')


def featurlist_Create(request):
    featurrlist = Featurelist.objects.all()
    myfrom = featurlistForm(request.POST or None, request.FILES or None)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'create-feuters.html', {"myfrom": myfrom,"featurrlist":featurrlist})


def getfeuterslistUpdate(request, pid):
    data=get_object_or_404(Featurelist,id=pid)
    myfrom = featurlistForm(request.POST or None, request.FILES or None,instance=data)
    if myfrom.is_valid():
        instance = myfrom.save(commit=False)
        instance.save();
        return redirect('index')
    return render(request, 'create-feuters.html', {"myfrom": myfrom,})

def getfeuterslistDelete(request, pid):
    data=get_object_or_404(Featurelist,id=pid)
    data.delete()
    return redirect('featurlistCreate')

class email(TemplateView):
    template_name = "email.html"
