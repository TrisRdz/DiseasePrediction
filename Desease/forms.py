from django import forms
from .models import user_registration
from .models import reg
from .models import feedback


class user_cr(forms.ModelForm):
    class Meta:
        model=user_registration
        fields=('Fname','Lname','Username','Email','Password')

class reg1(forms.ModelForm):
  class Meta:
    model=reg
    fields=('Drname','Department','Pnum')

class fb(forms.ModelForm):
  class Meta:
   model=feedback
   fields=('Name','Email','Message')

