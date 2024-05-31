from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)
admin.site.register(Blogs)
admin.site.register(ProgrammingLanguage)
admin.site.register(Post)
admin.site.register(Service)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ('fullname',
                    'usn',
                    'email',
                    'college_name',
                    'course',
                    'programming_langauge',
                    'timeStamp')
    search_fields=('fullname','usn','email')
    list_filter=['college_name','course','programming_langauge']

admin.site.register(Internship,InternshipAdmin)