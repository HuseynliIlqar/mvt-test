from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Index_Slider(models.Model):
    title=models.CharField(max_length=15)
    description = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    url = models.URLField(blank=True, null=True)

class Why_Choose_Us(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=100)
    img_box=models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class About_Container(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=500)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Trainers_Container(models.Model):
    trainer_name = models.CharField(max_length=30)
    trainer_image = models.ImageField(upload_to='images/')

    facebook_url = models.URLField(blank=True, null=True)
    facebook_img=models.ImageField(upload_to='images/', blank=True)

    twitter_url = models.URLField(blank=True, null=True)
    twitter_img=models.ImageField(upload_to='images/',blank=True)

    instagram_url = models.URLField(blank=True, null=True)
    instagram_img=models.ImageField(upload_to='images/',blank=True)

    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Info_Section(models.Model):
    item_name = models.CharField(max_length=50)
    item_url = models.URLField(blank=True, null=True)
    copy_info = models.CharField(max_length=50, blank=True, null=True)
    item_icon = models.ImageField(upload_to='images/',blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Shop(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)