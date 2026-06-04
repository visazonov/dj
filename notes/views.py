from django.shortcuts import render

from notes.models import Note


def list_notes_view(request):
    page_number = request.Get.get('page', 1)
    context = {
        'notes': Note.objects.prefetch_related('tags').select_related('user').all()
    }
    return render(request, 'notes/list.html', context)
