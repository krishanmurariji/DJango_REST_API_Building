from django.contrib import admin
from app.models import Group
from app.models import Car,Product,Storage,Name,Todo,Contacts

# Register your models here.
admin.site.register(Group)
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Storage)
admin.site.register(Name)
admin.site.register(Todo)
admin.site.register(Contacts)
