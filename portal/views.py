# fBSD-Community-Portal
# Copyright (c) 2011 Nolan Lum <nol888@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, Http404

from fBSD_Portal.portal.models import CommPortalProfile
from social_auth.models import UserSocialAuth

from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

import django.contrib.auth

AUTH_PROVIDERS = ['google', 'yahoo', 'linkedin', 'facebook']
PROFILE_FIELDS = [
                  ['Interests', 'interests', 'textarea', ''],
                  ['About me', 'about_me', 'textarea', ''],
                  ['When I\'m Free', 'free_time', 'input', ''],
                  ['Hobbies', 'hobbies', 'textarea', ''],
                  ['Tags', 'tags', 'input', '']
                 ]


@require_http_methods(['GET'])
@login_required
def index(request):
    d = {
         'last_login' : request.session.get('social_auth_last_login_backend'),
         'user_profile' : request.user.get_profile()
        }

    try:
        d['extra_data'] = UserSocialAuth.objects.get(pk=request.user.id).extra_data
    except UserSocialAuth.DoesNotExist:
        pass
    
    return render_to_response('index.html', d, RequestContext(request))

@require_http_methods(['GET'])
def login(request):
    d = { 'auths': AUTH_PROVIDERS }
    
    return render_to_response('login.html', d, RequestContext(request))

@require_http_methods(['GET'])
def logout(request):
    django.contrib.auth.logout(request)
    d = { 'redirect_url' : '/' }
    
    return render_to_response('logout.html', d, RequestContext(request))

@require_http_methods(['GET', 'POST'])
@login_required
@csrf_protect
def user(request, id):
    # Try to get a user.
    view_user = get_object_or_404(django.contrib.auth.models.User, pk=id)
    
    d = {
         'last_login' : request.session.get('social_auth_last_login_backend'),
         'can_edit' : request.user.id == int(id),
         'view_user' : view_user,
         'user_fields' : PROFILE_FIELDS,
        }

    # Try to get a profile; we should have one, as it's created on user create.
    try:
        prof = view_user.get_profile()
    except CommPortalProfile.DoesNotExist:
        raise Http404("User doesn't have a profile! Bug?")

    # If we can edit, and there is POSTDATA, update the profile.
    if request.POST and d['can_edit']:
        for x in PROFILE_FIELDS:
            setattr(prof, x[1], "" if request.POST[x[1]] == "None entered." else request.POST[x[1]] )
        prof.save()

    # Fill stuff with stuff.
    for x in d['user_fields']:
        x[3] = getattr(prof, x[1])

    # Render.
    return render_to_response('user.html', d, RequestContext(request))