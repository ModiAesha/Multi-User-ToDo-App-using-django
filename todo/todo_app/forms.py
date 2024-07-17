from django.forms import ModelForm
import datetime

from todo_app.models import Todo
class TODOForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title' , 'status' , 'priority']