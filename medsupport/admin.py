from django.contrib import admin
from .models import  (
    Hospital,  Contact,
    HospitalCategory, SolutionCategory,
    Solution, HospitalNeed,
    SolutionImage
)


class NeedInline(admin.TabularInline):
    model = HospitalNeed
    fields = ('solution', ('quantity_needed', 'quantity_received'), 'units',)
    autocomplete_fields = ['solution']
    extra = 1


class ContactInline(admin.TabularInline):
    model = Contact
    classes = ('collapse',)
    fields = ('hospital', 'full_name', 'position', 'phone', 'email')
    extra = 0


class SolutionImageInline(admin.TabularInline):
    verbose_name_plural = "Додаткові фото"
    model = SolutionImage
    extra = 1


@admin.register(SolutionCategory)
class SolutionCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ("Категорія", {
            'classes': ('collapse',),
            'fields': ('categories',)
        }),
        (None, {
            'fields': (('main_image', 'attachment'), 'instruction', ('materials', 'tools'), 'approved_by')
        })

    )
    search_fields = ('name',)
    filter_horizontal = ('categories',)
    inlines = (SolutionImageInline,)


@admin.register(HospitalNeed)
class NeedAdmin(admin.ModelAdmin):
    pass


@admin.register(HospitalCategory)
class HospitalCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Користувачі", {
            'classes': ('collapse',),
            'fields': ('users',)
        }),
        (None, {
            'fields': (('name', 'description'))
        }),
        ("Категорія установи", {
            'classes': ('collapse',),
            'fields': ('categories',)
        }),
        ("Адрес", {
            'classes': ('collapse',),
            'fields': (('region', 'city'), ('line1', 'zip_code'), ('geo_lat', 'geo_lng'))
        }),
        ("Додатково", {
            'classes': ('collapse',),
            'fields': (('company_code'), ('email'))
        }),
    )
    filter_horizontal = ('users','categories',)
    inlines = (ContactInline, NeedInline)

    def get_queryset(self, request):
        qs = super(HospitalAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(user=request.user)
        return qs

    def get_readonly_fields(self, request, obj=None):
        fields = list(super(HospitalAdmin, self).get_readonly_fields(request, obj))

        # add User field to read_only if user is not superuser
        if not request.user.is_superuser:
            fields.append('user')
        return fields
