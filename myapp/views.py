from django.shortcuts import render, redirect
from .models import Contact, Index_Slider, Why_Choose_Us, About_Container, Trainers_Container, Info_Section,Shop,Blog
from .forms import ContactForm
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string



def index(request):
    sliders = Index_Slider.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()
    about_container = About_Container.objects.all()
    trainers_container = Trainers_Container.objects.all()
    info_section = Info_Section.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            form.save()
            send_mail(
                subject='Neogym',
                message=f'{name} adlı istifadəçi sizə mesaj göndərdi:\n {message}',
                html_message=render_to_string('success.html'),
                from_email=EMAIL_HOST_USER,
                recipient_list=['ilqarhuseynli51@gmail.com'],
            )
            return redirect('success')
    else:
        form = ContactForm()

    return render(request,'index.html',{
        'sliders': sliders,
        'form': form,
        'why_choose_us': why_choose_us,
        'about_container': about_container,
        'trainers_container': trainers_container,
        'info_section': info_section
    })


def why_us(request):
    why_choose_us = Why_Choose_Us.objects.all()
    info_section = Info_Section.objects.all()
    return render(request, 'why_us.html', {
        'name': 'why_us',
        'why_choose_us': why_choose_us,
        'info_section': info_section
    })


def trainer(request):
    trainers_container = Trainers_Container.objects.all()
    info_section = Info_Section.objects.all()
    return render(request, 'trainer.html', {
        'name': 'trainer',
        'trainers_container': trainers_container,
        'info_section': info_section
    })


def contact(request):
    info_section = Info_Section.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            form.save()
            send_mail(
                subject='Neogym',
                message=f'{name} adlı istifadəçi sizə mesaj göndərdi:\n {message}',
                html_message=render_to_string('success.html'),
                from_email=EMAIL_HOST_USER,
                recipient_list=['ilqarhuseynli51@gmail.com'],
            )
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'info_section': info_section
    })


def blog_page(request):
    info_section = Info_Section.objects.all()
    return render(request, 'blog_page.html', {
        'name': 'read_more',
        'info_section': info_section
    })


def success_view(request):
    info_section = Info_Section.objects.all()
    return render(request, 'success.html', {
        'info_section': info_section
    })


def shop(request):
    shoping = Shop.objects.all()
    info_section = Info_Section.objects.all()
    return render(request, 'shop.html', {
        'name': 'shop',
        'shoping':shoping,
        'info_section': info_section
    })


def news(request):
    blog = Blog.objects.all()
    info_section = Info_Section.objects.all()
    return render(request, 'news.html', {
        'name': 'news',
        'blog': blog,
        'info_section': info_section
    })
