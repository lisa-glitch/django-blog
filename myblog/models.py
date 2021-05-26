from django.db import models

from django.contrib.auth.models import User

#Create Your Models here

class Category(models.Model):
    name= models.CharField(max_length=50, null=False, blank=False)
    parent_id= models.ForeignKey('Category',on_delete=models.CASCADE, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    upadated_at= models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return '%s' % (self.name)

class Tag(models.Model):
    name= models.CharField(max_length=100, null=False, blank=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Feedback(models.Model):
    message= models.TextField(null=False, blank=False)
    user_name= models.CharField(max_length=50, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class Post(models.Model):
    title= models.CharField(null=False, max_length=200, blank=False)
    post= models.TextField(null=False, blank=False)
    category_id= models.ForeignKey('Category', on_delete=models.CASCADE, blank=False, null=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return '%s' % (self.title)

class Comment(models.Model):
    rating= models.IntegerField(null=True, blank=True)
    post= models.TextField(null=True, blank=True,max_length=300)
    user_id= models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    post_id= models.ForeignKey('Post', blank=False, null=False, on_delete=models.CASCADE)

class Image(models.Model):
    image_url= models.CharField(max_length=200, blank=False, null=False)
    post_id= models.ForeignKey('Post', blank=False, null=False, on_delete=models.CASCADE)

class Share(models.Model):
    SOCIAL_SITES= (
        ('F','Facebook'),
        ('T','Twitter'),
        ('I','Instagram'),
        ('L','LinkedIn'),
        ('O','Other')
    )

    social_media= models.CharField(max_length=200, null=False, blank=False, choices=SOCIAL_SITES)
    user_id= models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE )
    post_id= models.ForeignKey('Post', blank=False, null=False, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    

