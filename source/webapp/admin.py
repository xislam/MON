from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from modeltranslation.admin import TabbedTranslationAdmin

from webapp.models import *


class NewsAdminForm(forms.ModelForm):

     class Meta:
        model = News
        fields = '__all__'

     class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'subtitle', 'status')
    search_fields = ['title', 'subtitle', 'status']
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)


class ContentOrganizationCategoryForm(forms.ModelForm):
    class Meta:
        model = ContentOrganizationCategory
        fields = '__all__'

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContentOrganizationCategoryAdmin(TabbedTranslationAdmin):
    list_display = ('category',)
    search_fields = ['category']
    form = ContentOrganizationCategoryForm


admin.site.register(ContentOrganizationCategory, ContentOrganizationCategoryAdmin)


class ContentOrganizationForm(forms.ModelForm):
    class Meta:
        model = ContentOrganization
        fields = '__all__'

        class Media:
            js = (
                'modeltranslation/js/force_jquery.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }


class ContentOrganizationAdmin(TabbedTranslationAdmin):
    list_display = ('category', 'title',)
    search_fields = ['category', 'title']
    form = ContentOrganizationForm


admin.site.register(ContentOrganization, ContentOrganizationAdmin)


class OrganizationStructureForm(forms.ModelForm):
    class Meta:
        model = OrganizationStructure
        fields = '__all__'

        class Media:
            js = (
                'modeltranslation/js/force_jquery.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }


class OrganizationStructureAdmin(TabbedTranslationAdmin):
    list_display = ('initials',)
    search_fields = ['initials']


admin.site.register(OrganizationStructure, OrganizationStructureAdmin)


class CategoryNPAForm(forms.ModelForm):
    class Meta:
        model = CategoryNPA
        fields = '__all__'

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class CategoryNPAAdmin(TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ['name']
    form = CategoryNPAForm


admin.site.register(CategoryNPA, CategoryNPAAdmin)


class NPAForm(forms.ModelForm):
    class Meta:
        model = NPA
        fields = '__all__'

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NPAAdmin(TabbedTranslationAdmin):
    list_display = 'title', 'subtitle',
    search_fields = ['title', 'subtitle']
    form = NPAForm


admin.site.register(NPA, NPAAdmin)


class LeadershipForm(forms.Form):
    class Meta:
        models = Leadership
        fields = '__all__'

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class LeadershipAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title',
        search_fields = ['title']
        form = LeadershipForm


admin.site.register(Leadership, LeadershipAdmin)


class StructureForm(forms.Form):
    class Meta:
        models = Structure
        fields = '__all__'

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class StructureAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'name',
        search_fields = ['name']
        form = Structure


admin.site.register(Structure, StructureAdmin)


