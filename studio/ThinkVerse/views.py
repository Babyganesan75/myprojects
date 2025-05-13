from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        mobile = request.POST.get('mobile')

        # Updated full message with mobile number
        full_message = (
            f"From: {name} <{email}>\n"
            f"Mobile: {mobile}\n\n"
            f"Message:\n{message}"
        )

        send_mail(
            subject='New Contact Message',
            message=full_message,
            from_email=email,
            recipient_list=['projectspro95@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('home')

    return render(request, 'index.html')
