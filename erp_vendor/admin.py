from django.contrib import admin
from .models import *

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):

    list_display = (
        "vendor_id",
        "vendor_name",
        "gst_number",
        "pan_number",
    )

    search_fields = (
        "vendor_id",
        "vendor_name",
    )

    list_filter = (
        "vendor_id",
        "vendor_name",
    )
    def __str__(self):
        return f"{self.vendor_id} - {self.vendor_name}"
