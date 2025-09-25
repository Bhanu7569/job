from django.http import HttpResponsePermanentRedirect
from django.utils.deprecation import MiddlewareMixin

class WwwRedirectMiddleware(MiddlewareMixin):
    """Redirect non-www to www."""
    def process_request(self, request):
        host = request.get_host()
        if host == 'jobifyworld.com':
            url = request.build_absolute_uri().replace('jobifyworld.com', 'www.jobifyworld.com', 1)
            return HttpResponsePermanentRedirect(url)
        return None


class AllowRobotsIndexMiddleware(MiddlewareMixin):
    """Ensure Google can index the site."""
    def process_response(self, request, response):
        # Only apply to HTML and sitemap XML responses
        content_type = response.get('Content-Type', '')
        if 'text/html' in content_type or 'xml' in content_type:
            response['X-Robots-Tag'] = 'index, follow'
        return response
