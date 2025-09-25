from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == 'jobifyworld.com':
            url = request.build_absolute_uri().replace('jobifyworld.com', 'www.jobifyworld.com', 1)
            return HttpResponsePermanentRedirect(url)
        return self.get_response(request)
