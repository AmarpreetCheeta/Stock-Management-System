from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class Useradmin(UserAdmin):
    list_display = ['id','email','username','first_name','phone','date_joined','last_login','is_staff','is_admin']
    search_fields = ['email','username','first_name','phone']
    readonly_fields = ['date_joined','last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []

admin.site.register(User, Useradmin)


class ProfileImgAdmin(admin.ModelAdmin):
    list_display = ['id','user','image']

admin.site.register(ProfileImg, ProfileImgAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','user','business_name','business_email','business_phone','business_website','business_address',
                    'type_of_entity','industry_type','business_type']

admin.site.register(UserInfoModel, UserInfoAdmin)


class PurchaseEntryAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_name','vendor_name','purchase_quantity','gst_number','purchase_date','purchase_price',
                'purchase_type']
admin.site.register(PurchaseEntryModel, PurchaseEntryAdmin)


class CustomerDetailAdmin(admin.ModelAdmin):
    list_display = ['id','user','image','customer_name','company_name','customer_address','gst_number','customer_phone','customer_email']
admin.site.register(CustomerDetailModel, CustomerDetailAdmin)    


class SalesEntryAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_name','customer_name','sales_quantity','gst_number','sales_date','sales_price','sales_type']
admin.site.register(SalesEntryModel, SalesEntryAdmin)   


class ProductListAdmin(admin.ModelAdmin):
    list_display = ['id','user','product_image','product_name','product_barcode','product_color','product_size',
                    'product_discription']
admin.site.register(ProductListModel,ProductListAdmin)                    


class VendorDetailAdmin(admin.ModelAdmin):
    list_display = ['id','user','image','vendor_name','company_name','vendor_address','gst_number','vendor_phone','vendor_email']
admin.site.register(VendorDetailModel, VendorDetailAdmin)    


class ExpansesListAdmin(admin.ModelAdmin):
    list_display = ['id','user','expanses_title','expanses_discription','expanses_date','expanses_amount']
admin.site.register(ExpansesListModel, ExpansesListAdmin)    