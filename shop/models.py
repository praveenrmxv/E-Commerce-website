from django.db import models

# Create your models here.
class Product(models.Model):
    objects = None
    product_id =models.AutoField
    product_name=models.CharField(max_length=500)
    category=models.CharField(max_length=50,default='0')
    subcategory=models.CharField(max_length=20,default='obc')
    price=models.IntegerField(default='0')
    desc=models.CharField(max_length=3000)
    pub_date=models.DateField(default='')
    image=models.ImageField(upload_to="image/",default='')
    def __str__(self):
        return self.product_name



class contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15, default='')
    desc = models.CharField(max_length=2000, default='')

    def _str_(self):
        return self.name




class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")






class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."


