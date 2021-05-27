from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Feedback)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Share)

