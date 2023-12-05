from django.contrib import admin
from .models import *
# Register your models here.


class NewsHashtagAdminList(admin.TabularInline):
    model = NewsHashtag
    
class NewsCategoryAdminList(admin.TabularInline):
    model = NewsCategory
    
# class NewsElementAdminList(admin.TabularInline):
#     model = NewsElement

class NewsThumbnillAdminList(admin.TabularInline):
    model = NewsThumbnill

class ElementAdminList(admin.TabularInline):
    model = Element
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsHashtagAdminList,NewsCategoryAdminList,ElementAdminList,NewsThumbnillAdminList]



    

    


admin.site.register(News,NewsAdmin)


admin.site.register((Category, Hashtag,NewsHashtag,Element,NewsCategory,NewsThumbnill))

