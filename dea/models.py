from django.db import models
from django.db.models.fields import DecimalField
from mptt.models import MPTTModel,TreeForeignKey
import datetime
from django.db.models import Avg, Count, Sum
from django.db.models.functions import Coalesce
# Create your models here.
# cr credit,dr debit
class TransactionType_DE(models.Model):
    XactTypeCode = models.CharField(max_length=2,primary_key=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# sundry_debtor,sundry_creditor,let desc be unique
class AccountType_Ext(models.Model):
    XactTypeCode = models.ForeignKey(TransactionType_DE ,
                        on_delete=models.CASCADE)
    description = models.CharField(max_length=100,unique = True)

    def __str__(self):
        return self.description

# person or organisation
class EntityType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# rameshbi,ramlalji,narsa
class Account(models.Model):
    entity = models.ForeignKey(EntityType,
                        null = True,
                        on_delete = models.SET_NULL)
    AccountType_Ext = models.ForeignKey(AccountType_Ext,
                        on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def current_balance(self,as_on='',):
        as_on = datetime.datetime.now()
        
        credit = self.accounttransaction_set\
                    .filter(XactTypeCode_ext__in = ['LG'])\
                    .aggregate(
                    t = Coalesce(Sum('Amount'),0))

        debit = self.accounttransaction_set\
                    .filter(XactTypeCode_ext__in = ['LR'])\
                    .aggregate(
                    t=Coalesce(Sum('Amount'),0))
        
        return credit['t'] - debit['t']

# account statement for ext account
class AccountStatement(models.Model):
    AccountNo = models.ForeignKey(Account,
                        on_delete = models.CASCADE)
    date = models.DateField(unique = True)
    ClosingBalance = models.DecimalField(max_digits=10, decimal_places=3)
    TotalCredit = models.DecimalField(max_digits=10, decimal_places=3)
    TotalDebit = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.AccountNo

# sales,purchase,receipt,payment
class TransactionType_Ext(models.Model):
    XactTypeCode_ext = models.CharField(max_length=3,primary_key= True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.XactTypeCode_ext

# ledger account type  for COA ,asset,liability,revenue,expense,gain,loss
class AccountType(models.Model):
    AccountType = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.AccountType

# import mptt here ledger is chart of accounts

class Ledger(MPTTModel):
    AccountType = models.ForeignKey(AccountType,
                    on_delete = models.CASCADE)
    name = models.CharField(max_length=100, unique = True)
    parent = TreeForeignKey('self',
                            null = True,
                            blank = True,
                            on_delete = models.CASCADE,
                            related_name = 'children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
    
    def current_balance(self):
        decendants = self.get_descendants(include_self = True)
        bal = [ acc.credit_txns.aggregate(t = Coalesce(Sum('amount'),0))['t']
                 - 
                acc.debit_txns.aggregate(t = Coalesce(Sum('amount'), 0))['t']
                    for acc in decendants]
        return sum(bal)

class LedgerTransaction(models.Model):
    ledger = models.ForeignKey(Ledger,on_delete =models.CASCADE ,related_name='credit_txns')
    date = models.DateTimeField(unique = True, auto_now_add = True)
    ledgerno_dr = models.ForeignKey(Ledger ,on_delete =models.CASCADE, related_name= 'debit_txns')
    amount = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.ledger.name

class LedgerStatement(models.Model):
    ledger = models.ForeignKey(Ledger,on_delete = models.CASCADE)
    date = models.DateField(unique = True)
    ClosingBalance = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.date


class AccountTransaction(models.Model):
    ledger = models.ForeignKey(Ledger,on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add= True,unique = True)
    XactTypeCode = models.ForeignKey(TransactionType_DE,
                    on_delete = models.CASCADE)
    XactTypeCode_ext = models.ForeignKey(TransactionType_Ext,
                        on_delete=models.CASCADE)
    Account = models.ForeignKey(Account,on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10,decimal_places=3)

    def __str__(self):
        return f"{self.XactTypeCode}"
