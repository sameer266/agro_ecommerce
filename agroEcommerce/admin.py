from django.contrib import admin
from .models import (UserProfile, UserRole, OTPVerification, Farmer, FarmerWallet, 
                     FarmerPayoutRequest, Vendor, VendorWallet, VendorPayoutRequest, 
                     AdminWallet, CommissionRate, Category, FarmerProduct, VendorProduct, 
                     Order, OrderItems, Cart, Review, AuditLog, Organization, Notification)

# Register models one by one
admin.site.register(UserProfile)
admin.site.register(UserRole)
admin.site.register(OTPVerification)
admin.site.register(Farmer)
admin.site.register(FarmerWallet)
admin.site.register(FarmerPayoutRequest)
admin.site.register(Vendor)
admin.site.register(VendorWallet)
admin.site.register(VendorPayoutRequest)
admin.site.register(AdminWallet)
admin.site.register(CommissionRate)
admin.site.register(Category)
admin.site.register(FarmerProduct)
admin.site.register(VendorProduct)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Cart)
admin.site.register(Review)
admin.site.register(AuditLog)
admin.site.register(Organization)
admin.site.register(Notification)
