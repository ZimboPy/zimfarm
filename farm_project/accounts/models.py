from django.db import models
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string


class UserDefaultAddress(models.Model):
	'''creates a default address for the farmer of customer'''
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	address = models.ForeignKey("UserAddress", null=True, blank=True, related_name="user_address_default")

	def __str__(self):
		return (self.user.username)



class UserAddressManager(models.Manager):
	'''this is the filter for all the address that are in the database'''
	def get_address(self, user):
		return super(UserAddressManager, self).filter(address=True).filter(user=user)



class UserAddress(models.Model):
	'''model to create an address'''
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120)
	province = models.CharField(max_length=120, null=True) # it will be good to add a choice
	phone = models.CharField(max_length=16)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.get_address()


	def get_address(self):
		return "%s, %s, %s" %(self.address, self.city, self.province)

	class Meta:
		ordering = ['updated', '-timestamp']


class EmailConfirmed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __str__(self):
		return self.confirmed

	def activate_user_email(self):
		activation_url = "%s%s" %(settings.SITE_URL, reverse("activation_view", args=[self.activation_key]))
		context = {"activation_key": self.activation_key, "activation_url": activation_url, "user": self.user.username}
		message = render_to_string("accounts/activation_message.txt", context)
		subject = "Activate your email"
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.User.email], kwargs)













# Create your models here.
