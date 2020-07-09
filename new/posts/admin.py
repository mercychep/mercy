from django.contrib import admin
from .models import Post
from .models import User


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    


admin.site.register(Post, PostAdmin)
admin.site.register(User)
