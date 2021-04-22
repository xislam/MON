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


@register(Leadership)
class Leadership(TranslationOptions):
    fields = 'title',


@register(Structure)
class Structure(TranslationOptions):
    fields = 'name',


@register(Position)
class Position(TranslationOptions):
    fields = 'description',


@register(Study)
class Study(TranslationOptions):
    fields = 'directions', 'document_type', 'author', 'file', 'name',


@register(Advertisement)
class Advertisement(TranslationOptions):
    fields = 'title', 'text', 'file',


@register(CategoryOC)
class CategoryOC(TranslationOptions):
    fields = 'name'


@register(StructureOC)
class StructureOC(TranslationOptions):
    fields = 'position'


@register(RegulationsOC)
class RegulationsOC(TranslationOptions):
    fields = 'description', 'file'


@register(RecommendationOC)
class RecommendationOC(TranslationOptions):
    fields = 'name', 'file',


@register(CorruptionCategory)
class CorruptionCategory(TranslationOptions):
    fields = 'name'


@register(Corruption)
class Corruption(TranslationOptions):
    fields = 'title', 'document_type', 'file',


@register(VacancyCategory)
class VacancyCategory(TranslationOptions):
    fields = 'name',


@register(Vacancy)
class Vacancy(TranslationOptions):
    fields = 'title', 'text', 'file',


@register(Contacts)
class Contacts(TranslationOptions):
    fields = 'title',


@register(Directory)
class Directory(TranslationOptions):
    fields = 'title',


@register(SUR)
class SUR(TranslationOptions):
    fields = 'title', 'file',

