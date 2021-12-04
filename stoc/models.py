from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have there email.")
        if not username:
            raise ValueError("Users must have there username.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )        

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )    

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email address',unique=True,max_length=200)
    username = models.CharField(max_length=70,verbose_name='Username',unique=True)
    first_name = models.CharField(max_length=150,verbose_name='Full name')
    phone = models.CharField(max_length=12,verbose_name='phone number',unique=True)
    date_joined = models.DateTimeField(verbose_name='Date_Joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last_login',auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name  

    def has_perm(self, perms, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True        


class ProfileImg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profileimg/%y')



TYPE_OF_ENTITY = [
    ('Individual','Individula'),
    ('Partnership','Partnership'),
    ('Public and Private Limited','Public and Private Limited'),
    ('Trust/Societies','Trust/Societies'),
    ('LLP','LLP'),
    ('Others','Others'),
    ('Unregistered Business','Unregistered Business'),
]


INDUSTRY_TYPE = [
    ('Textile','Textile'),
    ('Manufacturing','Manufacturing'),
    ('Banking/Finance Services','Banking/Finance Services'),
    ('Telecom/Telecom Equipments','Telecom/Telecom Equipments'),
    ('Export/Import','Export/Import'),
    ('Hospitality','Hospitality'),
    ('Construction','Construction'),
    ('Broker','Broker'),
    ('IT/ITes','IT/ITes'),
    ('Defence','Defence'),
    ('Cement','Cement'),
    ('Shopping','Shopping'),
    ('Retailling','Retailling'),
    ('Real Estate','Real Estate'),
    ('Airport','Airport'),
    ('Sugar','Sugar'),
    ('Tea','Tea'),
    ('Paper Product','Paper Product'),
    ('Rubber Product','Rubber Product'),
    ('Coal','Coal'),
    ('NBFC','NBFC'),
    ('Computer software','Computer software'),
    ('Hardware','Hardware'),
    ('Doctors','Doctors'),
    ('Agriculter','Agriculter'),
    ('Automobile','Automobile'),
    ('Furnitures','Furnitures'),
    ('Marketing','Marketing'),
    ('Water Supply','Water Supply'),
]

BUSINESS_TYPE = [
    ('Retailer','Retailer'),
    ('Wholesaler','Wholesaler'),
    ('Distributor','Distributor'),
    ('Manufacturer','Manufacturer'),
    ('Services','Services'),
    ('Others','Others'),
]


class UserInfoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=150)
    business_email = models.EmailField(max_length=250)
    business_phone = models.CharField(max_length=11)
    business_website = models.CharField(max_length=500)
    business_address = models.TextField()
    type_of_entity = models.CharField(choices=TYPE_OF_ENTITY,max_length=200)
    industry_type = models.CharField(choices=INDUSTRY_TYPE,max_length=200)
    business_type = models.CharField(choices=BUSINESS_TYPE,max_length=200)

    def __str__(self):
        return self.business_name

  
PAYMENT = [
    ('Debit','Debit'),
    ('Cheque','Cheque'),
    ('Cash','Cash'),
]


class CustomerDetailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customer_img/%y')
    customer_name = models.CharField(verbose_name='Customer Name',max_length=200)
    company_name = models.CharField(verbose_name='Company Name',max_length=300)
    customer_address = models.TextField(verbose_name='Customer Address',max_length=70)
    gst_number = models.IntegerField(verbose_name='GST Number')
    customer_phone = models.CharField(verbose_name='Customer Phone No.',max_length=11)
    customer_email = models.EmailField(verbose_name='Customer Email') 

    def __str__(self):
        return self.customer_name


class ProductListModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_img/%y')
    product_name = models.CharField(verbose_name='Product name',max_length=300)
    product_barcode = models.IntegerField(verbose_name='Product barcode')
    product_color = models.CharField(verbose_name='Product color',max_length=300)
    product_size = models.IntegerField(verbose_name='Product size')
    product_discription = models.TextField(verbose_name='Product discription',max_length=100)

    def __str__(self):
        return self.product_name


class SalesEntryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductListModel,on_delete=models.CASCADE)
    customer_name = models.ForeignKey(CustomerDetailModel,on_delete=models.CASCADE)
    sales_quantity = models.IntegerField(verbose_name='Sales quantity')
    gst_number = models.IntegerField(verbose_name='GST Number')
    sales_date = models.DateField(verbose_name='Sales date')
    sales_price = models.IntegerField(verbose_name='Sales price')
    sales_type = models.CharField(choices=PAYMENT,verbose_name='Sales type',max_length=100)


class VendorDetailModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='vendor_img/%y')
    vendor_name = models.CharField(verbose_name='Vendor name',max_length=300)
    company_name = models.CharField(verbose_name='Company name',max_length=300)
    vendor_address = models.TextField(verbose_name='Vendor address',max_length=100)
    gst_number = models.IntegerField(verbose_name='GST Number')
    vendor_phone = models.CharField(verbose_name='Vendor phone', max_length=11)
    vendor_email = models.EmailField(verbose_name='Vendor email')

    def __str__(self):
        return self.vendor_name


class PurchaseEntryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(ProductListModel,on_delete=models.CASCADE)
    vendor_name = models.ForeignKey(VendorDetailModel,on_delete=models.CASCADE)
    purchase_quantity = models.IntegerField(verbose_name='Purchase quantity')
    gst_number = models.IntegerField(verbose_name='GST Number')
    purchase_date = models.DateField(verbose_name='Purchase date')
    purchase_price = models.FloatField(verbose_name='Purchase price')
    purchase_type = models.CharField(verbose_name='Purchase type',max_length=100,choices=PAYMENT)


class ExpansesListModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expanses_title = models.CharField(verbose_name='Expenses Title',max_length=50)
    expanses_discription = models.TextField(verbose_name='Expenses Discription',max_length=150)
    expanses_date = models.DateField(verbose_name='Expenses Date')
    expanses_amount = models.IntegerField(verbose_name='Expenses Amount')
