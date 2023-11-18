from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def course(request):
    return render(request, 'courses.html')


def course_details(request):
    return render(request, 'course-details.html')


def trainers(request):
    return render(request, 'trainers.html')


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')


# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST["name"]
#         message_email = request.POST["email"]
#         message_subject = request.POST["subject"]
#         message = request.POST["message"]
#
#         # send an email
#         send_mail(
#             message_name,  # name
#             message_subject,  # subject
#             message,
#             message_email,  # To email
#             ['stephenonyango@students.must.ac.ke', 'ondeyostephen0@gmail.com'],  # to email
#         )
#
#         return render(request, 'contact.html', {})
#     else:
#         return render(request, 'contact.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # Send an email

        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # To email
            ['ondeyostephen0@gmail.com', 'stephenonyango@students.must.ac.ke', 'stephenomondi0@outlook.com'],
            # To email
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})
