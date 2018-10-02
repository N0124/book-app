from requests.models import Request


class RequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        Request.objects.create(path=request.path, method=request.method)

        response = self.get_response(request)

        return response
