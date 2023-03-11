from Dapp.models import Post
from django.contrib import admin
class saveformAdmin(admin.ModelAdmin):
    list_display=('name','email','message','post_date')
    
admin.site.register(Post,saveformAdmin)
# Register your models here.