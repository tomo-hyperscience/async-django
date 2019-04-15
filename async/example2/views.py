from django.http import StreamingHttpResponse

from .models import Person


def index(request):
    def generator():
        for i in range(30):
            for j in range(1000):
                person = Person(first_name='async', last_name='async')
                person.save()
            yield '.'
    return StreamingHttpResponse(generator())
