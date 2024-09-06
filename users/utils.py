from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

def sendAccessKey(otp, email, name):
    subject = "HRMS | Company Access Key"
    
    # Render the HTML email template with context
    html_message = render_to_string('email/otp_email.html', {'otp': otp, 'name': name})
    plain_message = strip_tags(html_message)  # Fallback to plain text
    from_email = 'professorcoding123@gmail.com'
    recipient_list = [email]

    # Use EmailMessage to send HTML email
    email_message = EmailMessage(subject, plain_message, from_email, recipient_list)
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()

def sendOtp(otp, email, name):
    subject = "HRMS | OTP Verification Code"
    
    # Render the HTML email template with context
    html_message = render_to_string('email/otp_email.html', {'otp': otp, 'name': name})
    plain_message = strip_tags(html_message)  # Fallback to plain text
    from_email = 'professorcoding123@gmail.com'
    recipient_list = [email]

    # Create the email message object
    email_message = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()
