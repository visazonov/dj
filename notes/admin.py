from django.contrib import admin

from notes.models import Note


# @admin.register(Note)
# class NoteAdmin(admin.ModelAdmin):
#     list_select_related = ['user']
#
#     def get_queryset(self, request):
#         return Note.objects.prefetch_related('tags').all()
