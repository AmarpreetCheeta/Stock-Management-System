from django.urls import path
from stoc import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/signup/',views.Signup,name='signup'),
    path('accounts/login/',views.LogIn,name='login'),
    path('',views.Home,name='home'), 

    path('purchase_entry/',views.PurchaseEntry.as_view(),name='purchase_entry'), 
    path('sales_entry/',views.Sales_Entry.as_view(),name='sales_entry'), 

    path('customer_detail/',views.Customer_Detail,name='customer_detail'), 
    path('customer_detail_add/',views.Custmer_Detail_Add.as_view(),name='customer_detail_add'),
    path('customer_detail_update/<customer_name>/',views.Customer_Detail_Update.as_view(),name='customer_detail_update'), 
    path('customer_data_delete/<int:id>/',views.Customer_Data_Delete,name='customer_data_delete'), 

    path('product_list/',views.Product_List,name='product_list'), 
    path('product_list_add/',views.Product_List_Add.as_view(),name='product_list_add'), 
    path('product_list_update/<product_name>/',views.Product_List_Update.as_view(),name='product_list_update'), 
    path('product_list_delete/<int:id>/',views.Product_List_Delete,name='product_list_delete'), 

    path('vendor_details/',views.Vendor_Details,name='vendor_details'), 
    path('vendor_details_add/',views.Vendor_Detail_Add.as_view(),name='vendor_details_add'), 
    path('vendor_details_update/<vendor_name>/',views.Vendor_Detail_Update.as_view(),name='vendor_details_update'), 
    path('vendor_details_delete/<int:id>/',views.Vendor_Details_Delete,name='vendor_details_delete'), 

    path('purchase_order/',views.PurchaseOrders.as_view(),name='purchase_order'),
    path('purchase_order_update/<int:pk>/',views.PurchaseOrderUpdate.as_view(),name='purchase_order_update'),
    path('purchase_order_delete/<int:pk>/',views.Purchase_order_delete,name='purchase_order_delete'),
    path('sales_order/',views.SalesOrders.as_view(),name='sales_order'),
    path('sales_order_update/<int:pk>/',views.SalesOrdersUpdate.as_view(),name='sales_order_update'),
    path('sales_order_delete/<int:pk>/',views.Sales_Order_Delete,name='sales_order_delete'),

    path('expenses_list',views.Expenses_List,name='expenses_list'),
    path('expenses_list_add',views.ExpensesListAdd.as_view(),name='expenses_list_add'),
    path('expenses_list_update/<expanses_title>/',views.ExpensesListUpdate.as_view(),name='expenses_list_update'),
    path('expenses_list_delete/<int:pk>/',views.Expenses_list_delete,name='expenses_list_delete'),

    path('profit_loss/',views.Profit_Loass,name='profit_loss'),
    
    path('profile/',views.Profile,name='profile'),
    path('profile_image/',views.Profile_Image,name='profile_image'),
    path('profileimg_update/<int:pk>/',views.Profileimg_Update,name='profileimg_update'),
    path('profile_img_delete/<int:pk>/',views.Profile_img_delete,name='profile_img_delete'),

    path('business_info/',views.User_Info,name='user_info'),
    path('business_infos/<business_name>/',views.User_info_update,name='user_info_update'),
    path('user_info_delete/<int:pk>/',views.User_info_delete,name='user_info_delete'),
    
    path('user_account/',views.User_Account,name='user_account'),

    path('change_password/',views.PasswordchangeClass.as_view(success_url='/change_password_done/'),name='change_password'),
    path('change_password_done/',views.Passwordchangedoneclass.as_view(),name='change_password_done'),

    path('delete_account/',views.Delete_Account,name='delete_account'),
    path('remove_account/<int:pk>/',views.Remove_User,name='remove_account'),

    path('search_product/', views.Search_for_Product, name='search_product'),
    path('search_vendor/', views.Search_for_Vendor, name='search_vendors'),
    path('search_customer/', views.Search_for_Customer, name='search_customer'),

    path('logout/',views.LogOutViews.as_view(),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)