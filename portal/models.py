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

from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CommPortalProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    interests = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    free_time = models.CharField(max_length=255, blank=True)
    hobbies = models.TextField(blank=True)
    tags = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.interests + self.about_me + self.free_time + self.hobbies + self.tags

@receiver(post_save, sender=User)
def CommPortalProfileCreate(sender, **kwargs):
    if kwargs['created']:
        CommPortalProfile.objects.create(user=kwargs['instance'])
    
class CommPortalPrivMsg(models.Model):
    user_from = models.ForeignKey(User, related_name='from')
    user_to = models.ForeignKey(User, related_name='to')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    read = models.BooleanField(default=False)
    notified = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s: %s" % (self.subject, self.body)

class CommPortalPMForm(forms.ModelForm):
    class Meta:
        model = CommPortalPrivMsg
        fields = ('subject', 'body')
        widgets = {
                   'subject' : forms.TextInput(attrs={'size' : 80, 'maxlength' : 255})
                  }
    