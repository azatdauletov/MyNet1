from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    activation_url = f"http://127.0.0.1:8000/v1/api/account/activate/{activation_code}"
    message = f"""
        Thank you for signing up.
        Activation link:{activation_url}
    """
    send_mail(
        'Activate your account',
        message,
        'admin@gmail.com',
        [email, ],
        fail_silently=False
    )
