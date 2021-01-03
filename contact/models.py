from django.db import models
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    
    # Fields
    name = models.CharField(max_length = 255)
    firstname = models.CharField(max_length = 255,blank = True)
    lastname = models.CharField(max_length = 255,blank = True)
    gender = models.CharField( max_length = 1,
                                choices = (('M','M'),('F','F'),('N','N')),
                                default = 'M')
    religion = models.CharField(max_length = 10,choices = (
                                ('Hindu','Hindu'),('Muslim','Muslim'),
                                ('Christian','Christian'),('Atheist','Atheist')
                                ),default = 'Hindu' )
    pic = models.ImageField(upload_to = 'contacts/customer/pic/', null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, editable = False)
    last_updated = models.DateTimeField(auto_now = True, editable = False)
    phonenumber = models.CharField(max_length=15,default = '911', verbose_name='Contact')
    Address = models.TextField(max_length=100,blank=True)
    ctype = (('Wh','Wholesale'),('Re','Retail'),('Su','Supplier'))
    type = models.CharField(max_length=30,choices=ctype,default='Re')
    ras = (('S/o','S/o'),('D/o','D/o'),('W/o','W/o'),('R/o','R/o'))
    relatedas = models.CharField(max_length=5,choices=ras,default='S/o')
    relatedto = models.CharField(max_length=30,blank=True)
    area = models.CharField(max_length=50,blank=True)
    active = models.BooleanField(blank = True,default = True)

    class Meta:
        ordering = ('-created','name','relatedto')
        unique_together = ('name','relatedas','relatedto')

    def __str__(self):
        return f"{self.name} {self.relatedas} {self.relatedto} {self.phonenumber}"

    def get_absolute_url(self):
        return reverse('contact_customer_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('contact_customer_update', args=(self.pk,))