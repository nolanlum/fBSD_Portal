from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from social_auth.models import UserSocialAuth

AUTH_PROVIDERS = ['google', 'yahoo', 'linkedin', 'facebook']

@require_http_methods(['GET'])
@login_required
def index(request):
    user = UserSocialAuth.objects.get(pk=request.user.id)
    
    t = loader.get_template('index.html')
    c = RequestContext(request, {  
                                 'last_login' : request.session.get('social_auth_last_login_backend'),
                                 'extra_data' : user.extra_data
                                })
    return HttpResponse(t.render(c))

@require_http_methods(['GET'])
def login(request):
    t = loader.get_template('login.html')
    c = RequestContext(request, {
                                 'auths': AUTH_PROVIDERS
                                })
    return HttpResponse(t.render(c))
