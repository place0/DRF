from tkinter.messagebox import NO
from django.contrib import admin
from .models import Note

admin.site.register(Note)