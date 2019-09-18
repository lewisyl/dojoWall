from __future__ import unicode_literals
from django.db import models
from apps.login_reg.models import User
import re

class PostManager(models.Manager):
    def post_msg_validator(self,postData):
        errors = {}
        if len(postData['post_message'])<5:
            errors['post_message'] = "Message should contain at least 5 charactors"
        return errors

    def post_cmt_validator(self,postData):
        errors = {}
        if len(postData['post_comment'])<5:
            errors['post_comment'] = " Comment should contain at least 5 charactors"
        return errors

class Messages(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="my_messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="my_comments")
    message = models.ForeignKey(Messages, related_name="commented_msg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

# class MessageForm(ModelForm):
#     class Meta:
#         model = Messages
#         fields = ['message']

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comment']