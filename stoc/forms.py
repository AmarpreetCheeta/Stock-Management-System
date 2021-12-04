from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm, PasswordChangeForm, PasswordResetForm,SetPasswordForm
from .models import *
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder':'Email address','class':'form-control'}
    ))
    phone = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder':'Phone number','class':'form-control'}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'Password','class':'form-control'}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'Confirm password','class':'form-control'}
    ))

    class Meta:
        model = User
        fields = ['email','username','first_name','phone']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Fullname','class':'form-control'}),
        }

        def clean_email(self):
            email = self.cleaned_data['email'].lower()
            try:
                account = User.objects.get(email=email)
            except Exception as e:
                return email
            raise ValidationError(f"Email {email} is already exists.")

        def clean_username(self):
            username = self.cleaned_data['username'].lower()
            try:
                account = User.objects.get(username=username)
            except Exception as e:
                return username
            raise ValidationError(f"Username {username} is already exists.")


class LoginCform(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder':'Email address','class':'form-control'}
    ))
    password = forms.CharField(widget= forms.PasswordInput(
        attrs={'placeholder':'Password', 'class':'form-control'}
    ))


class ProfileImgForm(forms.ModelForm):
    class Meta:
        model = ProfileImg
        fields = ['image']
        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control _yc3e','id':'Profil_id_img'})
        }


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfoModel
        fields = ['business_name','business_email','business_phone','business_website','business_address','type_of_entity','industry_type',
                    'business_type']     
        widgets = {
            'business_name':forms.TextInput(attrs={'placeholder':'Business name','class':'form-control', 'id':'inputPassword'}),
            'business_email':forms.EmailInput(attrs={'placeholder':'Business email','class':'form-control', 'id':'inputPassword'}),
            'business_phone':forms.NumberInput(attrs={'placeholder':'Business phone number','class':'form-control', 'id':'inputPassword'}),
            'business_website':forms.TextInput(attrs={'placeholder':'Business website','class':'form-control', 'id':'inputPassword'}),
            'business_address':forms.Textarea(attrs={'placeholder':'Country,state,city,','class':'form-control add_usr', 'id':'inputPassword'}),
            'type_of_entity':forms.Select(attrs={'placeholder':'Type of entity','class':'form-control', 'id':'inputPassword'}),
            'industry_type':forms.Select(attrs={'placeholder':'Industry type','class':'form-control', 'id':'inputPassword'}),
            'business_type':forms.Select(attrs={'placeholder':'business type','class':'form-control', 'id':'inputPassword'}),
        }           

YEAR = [i for i in range(1950,2022)]

class PurchaseEntryForm(forms.ModelForm):
    class Meta:
        model = PurchaseEntryModel
        fields = ['product_name','vendor_name','purchase_quantity','gst_number','purchase_date',
                'purchase_price','purchase_type']
        widgets = {
            'product_name':forms.Select(attrs={'placeholder':'Vendor name','class':'form-select _purch_', 'id':'inputPassword'}),
            'vendor_name':forms.Select(attrs={'placeholder':'Product name','class':'form-select _purch_', 'id':'inputPassword'}),
            'purchase_quantity':forms.NumberInput(attrs={'placeholder':'Purchase quantity','class':'form-control _purch_', 'id':'inputPassword'}),
            'gst_number':forms.NumberInput(attrs={'placeholder':'GST Number','class':'form-control _purch_', 'id':'inputPassword'}),
            'purchase_date':forms.SelectDateWidget(years=YEAR,attrs={'placeholder':'Purchase date','class':'_purch_ _h6C','id':'inputPassword'}),
            'purchase_price':forms.NumberInput(attrs={'placeholder':'Purchase price','class':'form-control _purch_', 'id':'inputPassword'}),
            'purchase_type':forms.Select(attrs={'placeholder':'Purchase type','class':'form-control _purch_', 'id':'inputPassword'}),
        }


class SalesEntryForm(forms.ModelForm):
    class Meta:
        model = SalesEntryModel
        fields = ['product_name','customer_name','sales_quantity','gst_number','sales_date',
                'sales_price','sales_type']
        widgets = {
            'product_name':forms.Select(attrs={'placeholder':'Product name','class':'form-select _purch_', 'id':'inputPassword'}),
            'customer_name':forms.Select(attrs={'placeholder':'Customer name','class':'form-select _purch_', 'id':'inputPassword'}),
            'sales_quantity':forms.NumberInput(attrs={'placeholder':'Sales quantity','class':'form-control _purch_', 'id':'inputPassword'}),
            'gst_number':forms.NumberInput(attrs={'placeholder':'GST Number','class':'form-control _purch_', 'id':'inputPassword'}),
            'sales_date':forms.SelectDateWidget(years=YEAR,attrs={'placeholder':'Sales date','class':'_purch_ _h6C', 'id':'inputPassword'}),
            'sales_price':forms.NumberInput(attrs={'placeholder':'Sales price','class':'form-control _purch_', 'id':'inputPassword'}),
            'sales_type':forms.Select(attrs={'placeholder':'Sales type','class':'form-control _purch_', 'id':'inputPassword'}),
        } 


class CustomerDetailForm(forms.ModelForm):
    class Meta:
        model = CustomerDetailModel
        fields = ['image','customer_name','company_name','customer_address','gst_number','customer_phone','customer_email']
        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control', 'id':'inputPassword'}),
            'customer_name':forms.TextInput(attrs={'placeholder':'Customer name','class':'form-control', 'id':'inputPassword'}),
            'company_name':forms.TextInput(attrs={'placeholder':'Company name','class':'form-control', 'id':'inputPassword'}),
            'customer_address':forms.Textarea(attrs={'placeholder':'Country,state,city','class':'form-control _ste4r', 'id':'inputPassword'}),
            'gst_number':forms.NumberInput(attrs={'placeholder':'GST Number','class':'form-control', 'id':'inputPassword'}),
            'customer_phone':forms.NumberInput(attrs={'placeholder':'Customer phone no.','class':'form-control', 'id':'inputPassword'}),
            'customer_email':forms.EmailInput(attrs={'placeholder':'Customer email','class':'form-control', 'id':'inputPassword'}),
        }

class ProductListForm(forms.ModelForm):
    class Meta:
        model = ProductListModel
        fields = ['product_image','product_name','product_barcode','product_color','product_size','product_discription']
        widgets = {
            'product_image':forms.FileInput(attrs={'class':'form-control _Pro_list'}),
            'product_name':forms.TextInput(attrs={'placeholder':'Product name','class':'form-control _Pro_list', 'id':'inputPassword'}),
            'product_barcode':forms.NumberInput(attrs={'placeholder':'Product barcode','class':'form-control _Pro_list', 'id':'inputPassword'}),
            'product_color':forms.TextInput(attrs={'placeholder':'Product color','class':'form-control _Pro_list', 'id':'inputPassword'}),
            'product_size':forms.NumberInput(attrs={'placeholder':'Product size','class':'form-control _Pro_list', 'id':'inputPassword'}),
            'product_discription':forms.Textarea(attrs={'placeholder':'Product discription','class':'form-control _Pro_list _ste4r', 'id':'inputPassword'}),
        }


class VendorDetailForm(forms.ModelForm):
    class Meta:
        model = VendorDetailModel
        fields = ['image','vendor_name','company_name','gst_number','vendor_address','vendor_phone','vendor_email']
        widgets = {
            'image':forms.FileInput(attrs={'class':'form-control', 'id':'inputPassword'}),
            'vendor_name':forms.TextInput(attrs={'placeholder':'Vendor name','class':'form-control', 'id':'inputPassword'}),
            'company_name':forms.TextInput(attrs={'placeholder':'Company name','class':'form-control', 'id':'inputPassword'}),
            'gst_number':forms.NumberInput(attrs={'placeholder':'GST Number','class':'form-control', 'id':'inputPassword'}),
            'vendor_address':forms.Textarea(attrs={'placeholder':'Country,state,city','class':'_ste4r form-control', 'id':'inputPassword'}),
            'vendor_phone':forms.NumberInput(attrs={'placeholder':'Vendor phone no.','class':'form-control', 'id':'inputPassword'}),
            'vendor_email':forms.EmailInput(attrs={'placeholder':'Vendor email','class':'form-control', 'id':'inputPassword'}),
        }


class ExpansesListForm(forms.ModelForm):
    class Meta:
        model = ExpansesListModel
        fields = ['expanses_title','expanses_discription','expanses_date','expanses_amount']
        widgets = {
            'expanses_title':forms.TextInput(attrs={'placeholder':'Expenses title','class':'form-control', 'id':'inputPassword'}),
            'expanses_discription':forms.Textarea(attrs={'placeholder':'Expenses discription','class':'form-control _ste4r', 'id':'inputPassword'}),
            'expanses_date':forms.SelectDateWidget(years=YEAR,attrs={'placeholder':'Expenses date','class':'_h6C', 'id':'inputPassword'}),
            'expanses_amount':forms.NumberInput(attrs={'placeholder':'Expenses amount','class':'form-control', 'id':'inputPassword'}),
        }

    
class Userchange_Form(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email','username','first_name','phone']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
        }


class PasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old Password",widget=forms.PasswordInput(
        attrs={'placeholder':'Old password','class':'form-control'}
    ))
    new_password1 = forms.CharField(label="New Password",widget=forms.PasswordInput(
        attrs={'placeholder':'New password','class':'form-control'}
    ))
    new_password2 = forms.CharField(label="Confirm new Password",widget=forms.PasswordInput(
        attrs={'placeholder':'Confirm password','class':'form-control'}
    ))