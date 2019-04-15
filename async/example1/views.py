import time

from django.http import StreamingHttpResponse


def index(request):
    def generator():
        for i in range(30):
            time.sleep(1)
            yield '.'
    return StreamingHttpResponse(generator())
