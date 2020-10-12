from django.contrib import admin
from .models import Products, Category, Evaluations, ImageUsers, TextSite, ImageProducts
from ckeditor.widgets import CKEditorWidget
from django import forms


class ProductsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Products
        fields = '__all__'


class ProductsAdmin(admin.ModelAdmin):
    form = ProductsAdminForm
    list_display = ('id', 'title', 'category', 'description', 'price', 'is_published', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class ImageProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'photos', 'photosmin')
    list_display_links = ('id', 'contact')
    search_fields = ('contact',)
    list_filter = ('contact',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class EvaluationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'contact', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


class ImageUsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'contact')
    list_display_links = ('id', 'contact')
    search_fields = ('contact',)
    list_filter = ('contact',)


class TextSiteAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = TextSite
        fields = '__all__'


class TextSiteAdmin(admin.ModelAdmin):
    form = TextSiteAdminForm
    list_display = ('id', 'header', 'text')
    list_display_links = ('id', 'header')
    search_fields = ('header', 'text')


admin.site.register(Products, ProductsAdmin)
admin.site.register(ImageProducts, ImageProductsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Evaluations, EvaluationsAdmin)
admin.site.register(ImageUsers, ImageUsersAdmin)
admin.site.register(TextSite, TextSiteAdmin)

