from django.contrib import admin

from .models import Restaurant, RestaurantImage, Tag, Certificate


class PostImageAdmin(admin.StackedInline):
    model = RestaurantImage


@admin.register(Restaurant)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Restaurant


@admin.register(RestaurantImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Certificate)
admin.site.register(Tag)
def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)
