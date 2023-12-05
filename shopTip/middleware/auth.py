from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect

class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path == '/accounts/login/' or \
            request.path == '/accounts/register/' or \
            'admin' in request.path or \
            request.user.is_authenticated:
            return response
        else:
            return HttpResponseRedirect('/accounts/login/')
