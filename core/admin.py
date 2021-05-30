from django.contrib import admin
from core.models import Contact,Portfolio
from django.utils.html import format_html
from django.utils.html import escape

admin.site.register(Contact)


class PortfolioInline(admin.TabularInline):
    model = Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    def delete (self, obj):
        return format_html('<input type="button" style="background-color:#ba2121;" value="Delete" onclick="location.href=\'{0}/delete/\'" />'.format(obj.pk))

    delete.allow_tags = True
    delete.short_description ='Delete Profolio'
    def image_tag(self,obj):
        if obj.get_image_video() =='mp4':
            return format_html(f'''
            <video width="320" height="180" controls>
            <source src="{obj.imageorvideo.url}" type="video/mp4">
            </video>
            ''')
        else:
            return format_html(f'<img src="{obj.imageorvideo.url}" alt="alt" width="320" height="180">')
       
    image_tag.allow_tags = True
    image_tag.short_description = 'Image / Video'
    list_per_page = 10
    search_fields = ("title","technology")
    list_display = ("title","technology","image_tag","uploaded_at","delete")
    list_editable = ("technology",)


admin.site.register(Portfolio,PortfolioAdmin)