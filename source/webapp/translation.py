from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'file', 'text', 'video',)


@register(ContentOrganizationCategory)
class ContentOrganizationCategory(TranslationOptions):
    fields = 'category',


@register(ContentOrganization)
class ContentOrganization(TranslationOptions):
    fields = 'title', 'text', 'img', 'video'


@register(OrganizationStructure)
class OrganizationStructure(TranslationOptions):
    fields = 'title',


@register(CategoryNPA)
class CategoryNPA(TranslationOptions):
    fields = 'name',


@register(NPA)
class NPA(TranslationOptions):
    fields = 'title', 'subtitle', 'document_type', 'file', 'text'

