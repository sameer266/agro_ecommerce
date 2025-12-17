
from django.urls import path,include


from . import views


urlpatterns = [
    path('',views.admin_dashboard,name='admin_dashboard_page'),
    
    # Orders
    path('orders/',views.order_list,name='admin_order_list_page'),
    path('order/pending/',views.order_pending_list,name='admin_order_pending_page'),
    path('order/delivered/',views.order_delivered_list,name='admin_order_delivered_page'),
    path('order-details/<int:order_id>/',views.order_details,name='admin_order_details'),
    
    
    # Farmer
    path('farmers/',views.farmer_list,name='admin_farmer_list_page'),
    path('farmer/edit/<int:farmer_id>/',views.farmer_edit,name='admin_farmer_edit_page'),
    path('farmer/delete/<int:farmer_id>/',views.farmer_delete,name='admin_farmer_delete'),
    path('farmer/products/<int:farmer_id>/',views.farmer_product_list,name='admin_farmer_products_list'),
    path('farmer-details/<int:farmer_id>/',views.farmer_details,name='admin_farmer_details_page'),
    path('farmer-kyc-pending/',views.farmer_kyc_pending,name='admin_farmer_kyc_pending_page'),
    path('farmer/payout-requests/',views.farmer_payout_requests,name='admin_farmer_payout_requests_page'),
    
    path('api/farmer-payment-payout-status-change/',views.FarmerPaymentPayoutStatusChangeAPIView.as_view(),name='admin_farmer_payout_status_change_api' ),
    path('api/farmer-kyc-status-change/',views.FarmerKYCChangeAPIView.as_view(),name='admin_farmer_kyc_change_api' ),
    
    
    # Vendor
    path('vendor/',views.vendor_list,name='admin_vendor_list_page'),
    path('vendor-details/<int:vendor_id>/',views.vendor_details,name='admin_vendor_details_page'),
    path('vendor/edit/<int:vendor_id>/',views.vendor_edit,name='admin_vendor_edit_page'),
    path('vendor/delete/<int:vendor_id>/',views.vendor_delete,name='admin_vendor_delete'),
    path('vendor/products/<int:vendor_id>/',views.vendor_product_list,name='admin_vendor_products_list'),
    path('api/vendor-kyc-status-change/',views.VendorKYCChangeAPIView.as_view(),name='admin_vendor_kyc_change_api'),
    
    
    
    
 
    
    
]

