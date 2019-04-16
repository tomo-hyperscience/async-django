import gevent
import os
import uuid

from django.http import HttpResponse, StreamingHttpResponse

from .models import Person


def index(request):
    def generator():
        for i in range(30):
            for j in range(1000):
                person = Person(first_name='async', last_name='async')
                person.save()
            yield '.'
    return StreamingHttpResponse(generator())


def connection(request):
    name = str(uuid.uuid4())[0:20]
    person = Person(first_name=name, last_name='async')
    person.save()
    return HttpResponse(name)


def file(request):
    def read_file_in_chunks(file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                file_object.close()
                break
            gevent.sleep()
            yield data
    f = open('/data/yourfile.zip', 'rb')
    response = StreamingHttpResponse(read_file_in_chunks(f))
    response['Content-Disposition'] = (
        'attachment; filename="yourfile.zip"')
    return response
