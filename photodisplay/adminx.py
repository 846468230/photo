from django.contrib import admin
from .models import UserProfile
from .models import Picture
from .models import Comment
from .models import Category
from .models import Honor
from .models import HomePhoto
import xadmin
# Register your models here.
class BaseAdmin(object):
    def get_list_queryset(self):
        request = self.request
        qs = super().get_list_queryset()
        return qs

@xadmin.sites.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('chinese_name','school','college','major')
    
@xadmin.sites.register(Picture)
class PictureAdmin(BaseAdmin):
    list_display = ('id','name','camera','focus','aperture','shutter_time','sensitive','status','created_time')
    
@xadmin.sites.register(Honor)
class HonorAdmin(BaseAdmin):
    list_display = ('owner','name','status','info_catogory')

@xadmin.sites.register(HomePhoto)
class HomePhotoAdmin(BaseAdmin):
    list_display = ('owner','title','subtitle','status','created_time')
#xadmin.sites.register(Picture)
@xadmin.sites.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display = ('target','nickname','email','status','created_time')

@xadmin.sites.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ('name','status','owner','created_time')