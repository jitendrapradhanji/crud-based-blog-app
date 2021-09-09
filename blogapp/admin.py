from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Newblog)
admin.site.register(Contact)


# Superuser Credentials
# admin username : Jitendra
# admin password : blog123
# admin email : pradhan.jitendra94@gmail.com
