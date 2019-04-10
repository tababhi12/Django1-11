from django.db import models
from django.db.models.signals import pre_save,post_save
import datetime as dt
from .utils import unique_slug_generator

# Create your models here.

class RestuarantLocation(models.Model):
    name = models.TextField(max_length=120)
    location = models.TextField(max_length=120,null = True,blank=True)
    category = models.CharField(max_length=120,null=True,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
    print('saving..')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    print(instance.timestamp)

# def rl_post_save_receiver(sender,instance,*args,**kwargs):
#     print('Saved')
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()
#     print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver,sender=RestuarantLocation)
#post_save.connect(rl_post_save_receiver,sender=RestuarantLocation)