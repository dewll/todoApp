from django.contrib import admin
from  todo.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
admin.site.register(Todo, TodoAdmin)

