from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from modeltranslation.admin import TabbedTranslationAdmin

from accounts.models import Role
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
    list_display = ['title', 'subtitle', 'status']
    raw_id_list_displayfields = ('user',)
    search_fields = ['title', 'subtitle', 'status']
    form = NewsAdminForm

    user_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'subtitle', 'img', 'file', 'text', 'video', 'status',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            if not request.user.is_superuser or not form.cleaned_data["user"]:
                obj.user = request.user
                obj.save()
            elif form.cleaned_data["user"]:
                obj.user = form.cleaned_data["user"]
                obj.save()

    def preprocess_list_display(self, request):
        if 'user' not in self.list_display:
            self.list_display.insert(self.list_display.__len__(), 'user')
        if not request.user.is_superuser:
            if 'user' in self.list_display:
                self.list_display.remove('user')

    def preprocess_search_fields(self, request):
        if 'user__username' not in self.search_fields:
            self.search_fields.insert(self.search_fields.__len__(), 'user__username')
        if not request.user.is_superuser:
            if 'user__username' in self.search_fields:
                self.search_fields.remove('user__username')

    def changelist_view(self, request, extra_context=None):
        self.preprocess_list_display(request)
        self.preprocess_search_fields(request)
        return super().changelist_view(request)

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            qs = super().get_queryset(request)
        return qs.filter(user=request.user)

    # def get_fieldsets(self, request, obj=None):
    #     if request.user.is_superuser:
    #         return super().get_fieldsets(request, obj)
    #     return self.user_fieldsets


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
        form = StructureForm


admin.site.register(Structure, StructureAdmin)


class PositionForm(forms.Form):
    class Meta:
        models = Position
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


class PositionAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'description',
        search_fields = ['description']
        form = PositionForm


admin.site.register(Position, PositionAdmin)


class StudyForm(forms.Form):
    class Meta:
        models = Study
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


class StudyAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'directions', 'document_type', 'author',
        search_fields = ['directions', 'document_type', 'author', 'file', 'name', ]
        form = StudyForm


admin.site.register(Study, StudyAdmin)


class AdvertisementForm(forms.Form):
    class Meta:
        models = Advertisement
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


class AdvertisementAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title' ]
        form = AdvertisementForm


admin.site.register(Advertisement, AdvertisementAdmin)


class CategoryOCForm(forms.Form):
    class Meta:
        models = CategoryOC
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


class CategoryOCAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'name'
        search_fields = ['name']
        form = CategoryOCForm


admin.site.register(CategoryOC, CategoryOCAdmin)


class StructureOCForm(forms.Form):
    class Meta:
        models = StructureOC
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


class StructureOCAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'position'
        search_fields = ['position']
        form = CategoryOCForm


admin.site.register(StructureOC, StructureOCAdmin)


class RegulationsOCForm(forms.Form):
    class Meta:
        models = RegulationsOC
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


class RegulationsOCAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'description'
        search_fields = ['description']
        form = CategoryOCForm


admin.site.register(RegulationsOC, RegulationsOCAdmin)


class RecommendationOCForm(forms.Form):
    class Meta:
        models = RecommendationOC
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


class RecommendationOCAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'name'
        search_fields = ['name']
        form = RecommendationOCForm


admin.site.register(RecommendationOC, RecommendationOCAdmin)


class CorruptionCategoryForm(forms.Form):
    class Meta:
        models = CorruptionCategory
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


class CorruptionCategoryAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'name'
        search_fields = ['name']
        form = CorruptionCategoryForm


admin.site.register(CorruptionCategory, CorruptionCategoryAdmin)


class CorruptionForm(forms.Form):
    class Meta:
        models = Corruption
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


class CorruptionAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title']
        form = CorruptionForm


admin.site.register(Corruption, CorruptionAdmin)


class VacancyCategoryForm(forms.Form):
    class Meta:
        models = VacancyCategory
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


class VacancyCategoryAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'name'
        search_fields = ['name']
        form = CorruptionForm


admin.site.register(VacancyCategory, VacancyCategoryAdmin)


class VacancyForm(forms.Form):
    class Meta:
        models = Vacancy
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


class VacancyAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title']
        form = VacancyForm


admin.site.register(Vacancy, VacancyAdmin)


class ContactsForm(forms.Form):
    class Meta:
        models = Contacts
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


class ContactsAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title']
        form = ContactsForm


admin.site.register(Contacts, ContactsAdmin)


class DirectoryForm(forms.Form):
    class Meta:
        models = Directory
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


class DirectoryAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title']
        form = DirectoryForm


admin.site.register(Directory, DirectoryAdmin)


class SURForm(forms.Form):
    class Meta:
        models = SUR
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


class SURAdmin(TabbedTranslationAdmin):
    class Meta:
        list_display = 'title'
        search_fields = ['title']
        form = SURForm


admin.site.register(SUR, SURAdmin)


@admin.register(Organization)
class Organization(admin.ModelAdmin):
    class Meta:
        list_display = 'name'
        search_fields = ['name']
