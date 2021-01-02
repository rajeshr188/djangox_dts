from django.db import models
from django.urls import reverse
import datetime
# Create your models here.
from tenant_schemas.models import TenantMixin

class Company(TenantMixin):
    name = models.CharField(max_length=100)
    paid_untill = models.DateField(blank = True,null = True)
    on_trial = models.BooleanField(default = True)
    created_on = models.DateField(auto_now_add = True)
    auto_create_Schema = True

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("org_company_detail", kwargs={"pk": self.pk})

    def set_paid_untill(self,date_or_timestamp):
        if isinstance(date_or_timestamp,int):
            self.paid_untill = datetime.date.fromtimestamp(date_or_timestamp)
        elif isinstance(date_or_timestamp,str):
            self.paid_untill = datetime.date.fromtimestamp(int(date_or_timestamp))
        else:
            self.paid_untill = date_or_timestamp
        self.save()
    
    def has_paid(self):
        if self.paid_untill is None:
            return False
        else:
            return datetime.datetime.today().date() < self.paid_untill 