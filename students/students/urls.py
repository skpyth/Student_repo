from django.contrib import admin
from django.urls import path
from studreg.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/register/',create_edit_new_course),
    path('edit/course/<int:crid>',fetch_course_info),
    path('delete/course/<int:crid>',delete_course_info),
]
