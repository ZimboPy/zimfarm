from django.contrib import admin
from .models import UserDefaultAddress, UserAddress, EmailConfirmed


class UserAddressAdmin(admin.ModelAdmin):
	class Meta:
		model = UserAddress


admin.site.register(UserAddress, UserAddressAdmin)

admin.site.register(UserDefaultAddress)

admin.site.register(EmailConfirmed)

# Register your models here.
