from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import RegexValidator

class Vendor(models.Model):
    vendor_id = models.CharField(max_length=20, unique=True)
    vendor_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    gst_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^[0-9A-Z]{15}$')],
        blank=True,
        null=True
    )
    pan_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$')],
        blank=True,
        null=True
    )
    ledger_code = models.CharField(max_length=50, blank=True)
    # is_msme_registered = models.BooleanField(default=False)