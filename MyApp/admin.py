from django.contrib import admin
from .models import MyProfile
from .models import Post
# Register your models here.
admin.site.register(MyProfile)
admin.site.register(Post)