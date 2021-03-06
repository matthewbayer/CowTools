from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, NewsletterSubscription, PressReleaseSubmission

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email', "first_name", "last_name", "password1", "password2", )

    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class SubscriptionForm(ModelForm):

    class Meta:
        model = NewsletterSubscription
        fields = ('email',)