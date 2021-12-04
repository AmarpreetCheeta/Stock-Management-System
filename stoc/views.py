from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.views import *
from django.views.generic import TemplateView
from .utils import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def Signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'Your account of EntryStock create successfully.')
                fm.save()
                return HttpResponseRedirect('/accounts/signup/')
        else:
            fm = SignUpForm()
        context = {'form':fm}            
        return render(request, 'registration/signup.html',context)  
    else:
        return HttpResponseRedirect('/')    


def LogIn(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginCform(request=request, data=request.POST)
            if fm.is_valid():
                em = fm.cleaned_data['username']
                pss = fm.cleaned_data['password']
                log = authenticate(email=em, password=pss)
                if log is not None:
                    login(request, log)
                    return HttpResponseRedirect('/')
        else:
            fm = LoginCform()
        return render(request, 'registration/login.html',{'forms':fm}) 
    else:
        return HttpResponseRedirect('/')    


@login_required
def Home(request):
    if request.user.is_authenticated:
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        context = {'profile_img':profile_img,'user_info_data':user_info_data}
        return render(request, 'stoc/home.html',context)
    else:
        return HttpResponseRedirect('/accounts/login/')


@method_decorator(login_required, name='dispatch')
class PurchaseEntry(TemplateView):
    def get(self, request):
        form = PurchaseEntryForm()
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        context = {'form':form,'profile_img':profile_img,'user_info_data':user_info_data}
        return render(request, 'stoc/purchase_entry.html',context)

    def post(self, request):
        form = PurchaseEntryForm(request.POST)
        if form.is_valid():
            user = request.user
            pro_n = form.cleaned_data['product_name']    
            ven_n = form.cleaned_data['vendor_name']    
            pur_q = form.cleaned_data['purchase_quantity']    
            pur_gst = form.cleaned_data['gst_number']    
            pur_d = form.cleaned_data['purchase_date']    
            pur_p = form.cleaned_data['purchase_price']    
            pur_t = form.cleaned_data['purchase_type']    
            reg = PurchaseEntryModel(user=user,product_name=pro_n,vendor_name=ven_n,purchase_quantity=pur_q,
                        gst_number=pur_gst,purchase_date=pur_d,purchase_price=pur_p,purchase_type=pur_t)                   
            messages.success(request, 'Your purchase entry data has been create successfully.')                    
            reg.save()
            return HttpResponseRedirect('/purchase_entry/')     


@method_decorator(login_required, name='dispatch')
class Sales_Entry(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        form = SalesEntryForm()
        context = {'profile_img':profile_img,'user_info_data':user_info_data,'form':form}
        return render(request, 'stoc/sales_entry.html',context)

    def post(self, request):
        form = SalesEntryForm(request.POST)
        if form.is_valid():
            user = request.user
            pro_n = form.cleaned_data['product_name']    
            cus_n = form.cleaned_data['customer_name']    
            sal_q = form.cleaned_data['sales_quantity']    
            sal_gst = form.cleaned_data['gst_number']    
            sal_d = form.cleaned_data['sales_date']    
            sal_p = form.cleaned_data['sales_price']    
            sal_t = form.cleaned_data['sales_type'] 
            reg = SalesEntryModel(user=user,product_name=pro_n,customer_name=cus_n,sales_quantity=sal_q,
                        gst_number=sal_gst,sales_date=sal_d,sales_price=sal_p,sales_type=sal_t)
            messages.success(request, 'Your Sales entry data has been create successfully.')             
            reg.save()     
            return HttpResponseRedirect('/sales_entry/')       


# This is Customer detail start:

@login_required
def Search_for_Customer(request):
    if request.method == 'GET':
        data = request.GET.get('search')
        data_search = CustomerDetailModel.objects.filter(customer_name__icontains=data)
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'customer_data':data_search, 'profile_img':profile_img,'user_info_data':user_info_data}
    return render(request, 'stoc/search_customer.html', context)

@login_required
def Customer_Detail(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    custmer_data = CustomerDetailModel.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'profile_img':profile_img,'customer_data':custmer_data,'user_info_data':user_info_data,}
    return render(request, 'stoc/customer_detail.html',context)

@method_decorator(login_required, name='dispatch')
class Custmer_Detail_Add(TemplateView):
    def get(self, request):
        form = CustomerDetailForm()
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        context = {'form':form,'profile_img':profile_img,'user_info_data':user_info_data}
        return render(request, 'stoc/customer_detail_add.html',context)  

    def post(self, request):
        form = CustomerDetailForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            user = request.user
            cust_img = form.cleaned_data['image']
            cust_nm = form.cleaned_data['customer_name']
            com_nm = form.cleaned_data['company_name']
            cus_add = form.cleaned_data['customer_address']
            cus_gst = form.cleaned_data['gst_number']
            cust_ph = form.cleaned_data['customer_phone']
            cust_em = form.cleaned_data['customer_email']
            reg = CustomerDetailModel(user=user,image=cust_img,customer_name=cust_nm,company_name=com_nm,
                        gst_number=cus_gst,customer_address=cus_add,customer_phone=cust_ph,customer_email=cust_em)
            messages.success(request, 'Your Customer data has been create successfully.')            
            reg.save()          
            return HttpResponseRedirect('/customer_detail_add/')  


@method_decorator(login_required, name='dispatch')
class Customer_Detail_Update(TemplateView):
    def get(self, request, customer_name):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        customer_data = CustomerDetailModel.objects.get(customer_name=customer_name)
        form = CustomerDetailForm(instance=customer_data)
        context = {'profile_img':profile_img,'form':form,'user_info_data':user_info_data}
        return render(request, 'stoc/customer_detail_add.html',context)

    def post(self, request, customer_name):
        customer_data = CustomerDetailModel.objects.get(customer_name=customer_name)
        form = CustomerDetailForm(data=request.POST,files=request.FILES,instance=customer_data)
        if form.is_valid():
            form.save()    
            return HttpResponseRedirect('/customer_detail/')   


@login_required
def Customer_Data_Delete(request, id):
    if request.method == 'POST':
        customer_data = CustomerDetailModel.objects.get(pk=id)
        customer_data.delete()
        return HttpResponseRedirect('/customer_detail/')

# This is Customer detail end

# This is Product list start


@login_required
def Search_for_Product(request):
    if request.method == 'GET':
        data = request.GET.get('search')
        data_search = ProductListModel.objects.filter(product_name__icontains=data)
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'search_data':data_search, 'profile_img':profile_img,'user_info_data':user_info_data}
    return render(request, 'stoc/search_product.html', context)


@login_required
def Product_List(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    product_data = ProductListModel.objects.filter(user=request.user)
    context = {'profile_img':profile_img,'user_info_data':user_info_data,'product_data':product_data}
    return render(request, 'stoc/product_list.html',context)


@method_decorator(login_required, name='dispatch')
class Product_List_Add(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        form = ProductListForm()
        context = {'profile_img':profile_img,'user_info_data':user_info_data,'form':form}
        return render(request, 'stoc/product_list_add.html',context)

    def post(self, request):
        form = ProductListForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = request.user
            pro_img = form.cleaned_data['product_image']
            pro_nm = form.cleaned_data['product_name']
            pro_br = form.cleaned_data['product_barcode']
            pro_col = form.cleaned_data['product_color']
            pro_siz = form.cleaned_data['product_size']
            pro_disc = form.cleaned_data['product_discription']
            reg = ProductListModel(user=user,product_image=pro_img,product_name=pro_nm,product_barcode=pro_br,
                                product_color=pro_col,product_size=pro_siz,product_discription=pro_disc)
            messages.success(request, 'Your Product List has been create successfully.')    
            reg.save()
            return HttpResponseRedirect('/product_list_add/')  

@method_decorator(login_required, name='dispatch')
class Product_List_Update(TemplateView):
    def get(self, request, product_name):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        product_data = ProductListModel.objects.get(product_name=product_name)
        form = ProductListForm(instance=product_data)
        context = {'profile_img':profile_img,'user_info_data':user_info_data,'form':form}
        return render(request, 'stoc/product_list_add.html',context)  

    def post(self, request, product_name):
        product_data = ProductListModel.objects.get(product_name=product_name)
        form = ProductListForm(data=request.POST,files=request.FILES,instance=product_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product_list/')      

def Product_List_Delete(request, id):
    if request.method == 'POST':
        product_data = ProductListModel.objects.get(pk=id)  
        product_data.delete()
        return HttpResponseRedirect('/product_list/')                                    

# This is Product list end

# This is Vendor detail start

@login_required
def Search_for_Vendor(request):
    if request.method == 'GET':
        data = request.GET.get('search')
        data_search = VendorDetailModel.objects.filter(vendor_name__icontains=data)
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'vendor_data':data_search,'profile_img':profile_img,'user_info_data':user_info_data}
    return render(request, 'stoc/search_vendor.html', context)

@login_required
def Vendor_Details(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    vendor_date = VendorDetailModel.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'profile_img':profile_img,'vendor_data':vendor_date,'user_info_data':user_info_data}
    return render(request, 'stoc/vendor_detail.html',context)


@method_decorator(login_required, name='dispatch')
class Vendor_Detail_Add(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        form = VendorDetailForm()
        context = {'profile_img':profile_img,'form':form,'user_info_data':user_info_data}
        return render(request, 'stoc/vendor_detail_add.html',context)    

    def post(self, request):
        form = VendorDetailForm(data=request.POST, files=request.FILES) 
        if form.is_valid():
            user = request.user
            ven_img = form.cleaned_data['image']
            ven_nm = form.cleaned_data['vendor_name']   
            com_nm = form.cleaned_data['company_name']   
            ven_add = form.cleaned_data['vendor_address']   
            ven_gst = form.cleaned_data['gst_number']   
            ven_ph = form.cleaned_data['vendor_phone']   
            ven_em = form.cleaned_data['vendor_email']
            reg = VendorDetailModel(user=user,image=ven_img,vendor_name=ven_nm,company_name=com_nm,vendor_address=ven_add,
                        gst_number=ven_gst,vendor_phone=ven_ph,vendor_email=ven_em)
            reg.save()
            messages.success(request, 'Your Vendor data has been create successfully.')
            return HttpResponseRedirect('/vendor_details_add/')

@method_decorator(login_required, name='dispatch')
class Vendor_Detail_Update(TemplateView):
    def get(self, request, vendor_name):
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        profile_img = ProfileImg.objects.filter(user=request.user)
        vendor_date = VendorDetailModel.objects.get(vendor_name=vendor_name)
        form = VendorDetailForm(instance=vendor_date)
        context = {'profile_img':profile_img,'form':form,'user_info_data':user_info_data}
        return render(request, 'stoc/vendor_detail_add.html',context)     

    def post(self, request, vendor_name):
        vendor_date = VendorDetailModel.objects.get(vendor_name=vendor_name)
        form = VendorDetailForm(data=request.POST, files=request.FILES, instance=vendor_date)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vendor_details/')           

def Vendor_Details_Delete(request, id):
    if request.method == 'POST':
        vendor_data = VendorDetailModel.objects.get(pk=id)
        vendor_data.delete()
        return HttpResponseRedirect('/vendor_details/')


# This is Vendor detail end

# This is purchase & sales orders start

@method_decorator(login_required, name='dispatch')
class PurchaseOrders(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        purchase_data = PurchaseEntryModel.objects.filter(user=request.user)
        context = {'user_info_data':user_info_data,'profile_img':profile_img,'purchase_data':purchase_data}
        return render(request, 'stoc/purchase_order.html',context)

@method_decorator(login_required, name='dispatch')
class PurchaseOrderUpdate(TemplateView):
    def get(self, request, pk):
        purchase_data = PurchaseEntryModel.objects.get(pk=pk)
        form = PurchaseEntryForm(instance=purchase_data)
        context = {'form':form}
        return render(request, 'stoc/purchase_entry.html',context)   

    def post(self, request, pk):
        purchase_data = PurchaseEntryModel.objects.get(pk=pk)
        form = PurchaseEntryForm(request.POST, instance=purchase_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/purchase_order/')

def Purchase_order_delete(request, pk):
    if request.method == 'POST':
        purchase_data = PurchaseEntryModel.objects.get(pk=pk)
        purchase_data.delete()
        return HttpResponseRedirect('/purchase_order/')           

@method_decorator(login_required, name='dispatch')
class SalesOrders(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        sales_data = SalesEntryModel.objects.filter(user=request.user)
        context = {'user_info_data':user_info_data,'profile_img':profile_img,'sales_data':sales_data}
        return render(request, 'stoc/sales_order.html',context)

@method_decorator(login_required, name='dispatch')
class SalesOrdersUpdate(TemplateView):
    def get(self, request, pk):
        salesorder_data = SalesEntryModel.objects.get(pk=pk)
        form = SalesEntryForm(instance=salesorder_data)
        context = {'form':form}
        return render(request, 'stoc/sales_entry.html',context)

    def post(self, request, pk):
        salesorder_data = SalesEntryModel.objects.get(pk=pk)
        form = SalesEntryForm(request.POST, instance=salesorder_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sales_order/')        

def Sales_Order_Delete(request, pk):
    if request.method == 'POST':
        salesorder_data = SalesEntryModel.objects.get(pk=pk)
        salesorder_data.delete()
        return HttpResponseRedirect('/sales_order/')

# This is purchase & sales orders end

# This is Expanses list start

@login_required
def Expenses_List(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    expenses_data = ExpansesListModel.objects.filter(user=request.user)
    context = {'user_info_data':user_info_data,'profile_img':profile_img,'expenses_data':expenses_data}
    return render(request, 'stoc/expenses_list.html',context)


@method_decorator(login_required, name='dispatch')
class ExpensesListAdd(TemplateView):
    def get(self, request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        form = ExpansesListForm(request.POST)
        context = {'user_info_data':user_info_data,'profile_img':profile_img,'form':form}
        return render(request, 'stoc/expenses_list_add.html',context)

    def post(self, request):
        form = ExpansesListForm(request.POST)
        if form.is_valid():
            user = request.user
            expanses_title = form.cleaned_data['expanses_title']
            expanses_discription = form.cleaned_data['expanses_discription']
            expanses_date = form.cleaned_data['expanses_date']
            expanses_amount = form.cleaned_data['expanses_amount']
            reg = ExpansesListModel(user=user,expanses_title=expanses_title,expanses_discription=expanses_discription,
                    expanses_date=expanses_date,expanses_amount=expanses_amount)
            messages.success(request, 'Your Expenses list has been create successfully.')         
            reg.save()        
            return redirect('expenses_list_add')

@method_decorator(login_required, name='dispatch')
class ExpensesListUpdate(TemplateView):
    def get(self, request, expanses_title):
        expenses_data = ExpansesListModel.objects.get(expanses_title=expanses_title)
        form = ExpansesListForm(instance=expenses_data)
        context = {'form':form}
        return render(request, 'stoc/expenses_list_add.html',context)

    def post(self, request, expanses_title):
        expenses_data = ExpansesListModel.objects.get(expanses_title=expanses_title)
        form = ExpansesListForm(request.POST,instance=expenses_data)
        if form.is_valid():
            form.save()
            return redirect('expenses_list')

def Expenses_list_delete(request, pk):
    if request.method == 'POST':
        expenses_data = ExpansesListModel.objects.get(pk=pk)
        expenses_data.delete()
        return redirect('expenses_list')

# This is Expanses list end

# This is profit and loss start

@login_required
def Profit_Loass(request):
    purchase = 0.0
    items = PurchaseEntryModel.objects.filter(user=request.user)
    tot_purchase = sum(items.values_list('purchase_price', flat=True))
    quantity_pur = sum(items.values_list('purchase_quantity', flat=True))
    total_am = tot_purchase * quantity_pur
    purchase += total_am

    expenses = 0.0
    ex_items = ExpansesListModel.objects.filter(user=request.user)
    tot_expense = sum(ex_items.values_list('expanses_amount', flat=True))  
    expenses += tot_expense

    sales = 0.0
    sal_items = SalesEntryModel.objects.filter(user=request.user)
    tot_sales = sum(sal_items.values_list('sales_price', flat=True))
    quantity_sal = sum(sal_items.values_list('sales_quantity', flat=True))
    total_sal_am = tot_sales * quantity_sal
    sales += total_sal_am

    tot_profit = sales

    loss_tot = 0.0
    loss_tot = purchase + expenses - sales 

    x = [x.purchase_date for x in items]
    y = [y.purchase_price for y in items]

    chart = pur_plot(x, y)

    p = [p.sales_date for p in sal_items]
    q = [q.sales_price for q in sal_items]

    sal_chart = sal_plot(p, q)

    a = [a.expanses_date for a in ex_items]
    b = [b.expanses_amount for b in ex_items]

    ex_chart = ex_plot(a, b)

    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'user_info_data':user_info_data,'profile_img':profile_img, 'purchase_amounts':purchase,
              'expenses_amounts':expenses, 'sales_amounts':sales, 'profit':tot_profit, 'chart':chart,
               'sal_chart':sal_chart, 'ex_chart':ex_chart, 'loss_tot':loss_tot}
    return render(request, 'stoc/profit_loss.html',context)

# This is profit and loss end

@login_required
def Profile(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'user_info_data':user_info_data,'profile_img':profile_img}
    return render(request, 'stoc/profile.html',context)


@login_required
def Profile_Image(request):
    if request.method == 'POST':
        fm = ProfileImgForm(data=request.POST,files=request.FILES)
        if fm.is_valid():
            user = request.user
            uimg = fm.cleaned_data['image']
            proceed = ProfileImg(user=user,image=uimg)
            proceed.save()
            return redirect('profile')
    else:
        fm = ProfileImgForm()
    user_info_data = UserInfoModel.objects.filter(user=request.user)    
    context = {'form':fm,'user_info_data':user_info_data}            
    return render(request, 'stoc/profile_image.html',context)

@login_required
def Profileimg_Update(request, pk):
    if request.method == 'POST':
        profile_img_data = ProfileImg.objects.get(pk=pk)
        fm = ProfileImgForm(data=request.POST,files=request.FILES,instance=profile_img_data)
        if fm.is_valid():
            fm.save()
            return redirect('profile')
    else:
        profile_img_data = ProfileImg.objects.get(pk=pk)
        fm = ProfileImgForm(instance=profile_img_data)
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'form':fm,'profile_img':profile_img,'user_info_data':user_info_data}    
    return render(request, 'stoc/profileimg_update.html',context)

def Profile_img_delete(request, pk):
    if request.method == 'POST':
        profile_img_data = ProfileImg.objects.get(pk=pk)
        profile_img_data.delete()
        return redirect('profile')


@login_required
def User_Info(request):
    if request.method == 'POST':
        fm = UserInfoForm(request.POST)
        if fm.is_valid():
            user = request.user
            ubn = fm.cleaned_data['business_name']
            uem = fm.cleaned_data['business_email']
            uph = fm.cleaned_data['business_phone']
            uweb = fm.cleaned_data['business_website']
            uadd = fm.cleaned_data['business_address']
            utoe = fm.cleaned_data['type_of_entity']
            uit = fm.cleaned_data['industry_type']
            ubt = fm.cleaned_data['business_type']
            reg = UserInfoModel(user=user,business_name=ubn,business_email=uem,business_phone=uph,business_website=uweb,
                            business_address=uadd,type_of_entity=utoe,industry_type=uit,business_type=ubt)
            reg.save()
            return redirect('user_info_update', reg.business_name)
    else:
        fm = UserInfoForm()
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'form':fm,'profile_img':profile_img,'user_info_data':user_info_data}                               
    return render(request, 'stoc/user_info.html',context)


@login_required
def User_info_update(request ,business_name):
    if request.method == 'POST':
        data = UserInfoModel.objects.get(business_name=business_name)
        form = UserInfoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('user_info_update', data.business_name)
    else:
        data = UserInfoModel.objects.get(business_name=business_name)
        form = UserInfoForm(instance=data)
    user_data = User.objects.filter()    
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)    
    context = {'user_data':user_data,'form':form,'user_info_data':user_info_data,'profile_img':profile_img}    
    return render(request, 'stoc/user_info.html',context)


def User_info_delete(request, pk):
    if request.method == 'POST':
        data = UserInfoModel.objects.get(pk=pk)
        data.delete()
        return HttpResponseRedirect('/business_info/')

@login_required
def User_Account(request):
    if request.method == 'POST':
        form = Userchange_Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_account/')
    else:
        form = Userchange_Form(instance=request.user)    
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user) 
    context = {'form':form,'profile_img':profile_img,'user_info_data':user_info_data}
    return render(request, 'stoc/user_account.html',context)

@login_required
def Delete_Account(request):
    profile_img = ProfileImg.objects.filter(user=request.user)
    user_info_data = UserInfoModel.objects.filter(user=request.user)
    context = {'profile_img':profile_img,'user_info_data':user_info_data}
    return render(request, 'stoc/delete_account.html',context)


def Remove_User(request, pk):
    if request.method == 'POST':
        User_account = User.objects.filter(pk=pk)
        User_account.delete()
        return HttpResponseRedirect('/accounts/login/')


@method_decorator(login_required, name='dispatch')
class PasswordchangeClass(PasswordChangeView):
    def get(self,request):
        form = PasswordchangeForm(request.POST)
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        context = {'form':form,'profile_img':profile_img,'user_info_data':user_info_data}
        return render(request, 'stoc/change_password.html',context)


@method_decorator(login_required, name='dispatch')
class Passwordchangedoneclass(PasswordChangeDoneView):
    def get(self,request):
        profile_img = ProfileImg.objects.filter(user=request.user)
        user_info_data = UserInfoModel.objects.filter(user=request.user)
        context = {'profile_img':profile_img,'user_info_data':user_info_data}
        return render(request, 'stoc/change_password_done.html',context)
        

@method_decorator(login_required, name='dispatch')
class LogOutViews(LogoutView):
    next_page = '/accounts/login/'