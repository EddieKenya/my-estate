from django.db import models
import random
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return(
         super(PropertyPublishedManager, self).get_queryset().filter(published_status=True)
        )
    
class Property(TimeStampedUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE = "FOR SALE", _("For sale")
        FOR_RENT = "FOR RENT", _("For Rent")
        AUCTION = "AUCTION", _("For Auctiom")
        AIRBNB = "AIRBNB", _("Airbnb")

    class PropertyType(models.TextChoices):
        BUNGALOW = 'BUNGALOW', _("Bungalow")
        COMMERCIAL = 'COMMERCIAL', _('Commercial')
        CONDOMINIUM = 'CONDOMINIUM', _('Condominium')
        COTTAGE = 'COTTAGE', _('Cottage')
        DUPLEX = 'DUPLEX', _('Duplex')
        FARMHOUSE = 'FARMHOUSE', _('Farm House')
        MANSION = 'MANSION', _('Mansion')
        MOBILEHOME = 'MOBILEHOME', _('Mobile Home')
        OFFICE = 'OFFICE', _('Office')
        PENTHOUSE = 'PENTHOUSE', _('Penthouse')
        STUDIO_APARTMENT = 'STUDIO', _('Studio Apartment')
        TOWNHOUSE = 'TOWNHOUSE', _('Town House')
        VILLA = 'VILLA', _('Villa')
        WAREHOUSE = "WAREHOUSE", _('Warehouse')
        OTHER = "OTHER", _("Other")

    
    user = models.ForeignKey(User, verbose_name=_("Agent, Seller or Buyer"), related_name='agent_buyer', on_delete=models.DO_NOTHING ),
    title = models.CharField(verbose_name=_("Property Title"), max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=True )
    ref_code = models.CharField(verbose_name=_('Property Reference Code'), max_length=255, unique=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), default="What's unique about this property....")
    country = CountryField(verbose_name=('Country'), default="KE", blank_label ="(select country)",)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Nairobi")
    postal_code = models.CharField(verbose_name= _("Postal Code"), max_length=100, default="140")
    street_address = models.CharField(verbose_name=_("Street Address"), max_length=150, default='Kenyatta Avenue')
    property_number = models.IntegerField(verbose_name= _('Property Number'), validators=[MinValueValidator(1)], default=112)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=8, decimal_places=2, default=0.00)
    tax = models.DecimalField(verbose_name=_('Property Tax'), max_digits=8, decimal_places=2, default=0.15, help_text="15% residential tax",)
    plot_area = models.DecimalField(verbose_name=_("Property Area(meters squared)"), max_digits=8, decimal_places=2, default=0.0)
    total_floors = models.IntegerField(verbose_name=_("Number of floors"), default=0)
    bedrooms = models.IntegerField(verbose_name=_('Bedrooms'), default=1)
    bathrooms = models.DecimalField(verbose_name=_('Bathrooms'), max_digits=20, decimal_places=2, default=1.0)
    advert_type= models.CharField(verbose_name= _("Advert Type"), max_length=100, choices=AdvertType.choices, default=AdvertType.FOR_SALE,)
    property_type = models.CharField(verbose_name= _("Property Type"), max_length=50, choices=PropertyType.choices, default=PropertyType.MANSION)
    cover_photo = models.ImageField( verbose_name= _("Property Photo"), default="kijani.jpg", null=True, blank=True)
    photo1 = models.ImageField(default="interior.jpg" ,null=True, blank=True)
    photo2 = models.ImageField(default="dishi.jpg" ,null=True, blank=True)
    photo3 = models.ImageField(default="bedroom.jpg" ,null=True, blank=True)
    photo4 = models.ImageField(default="dining.jpg" ,null=True, blank=True)
    published_status = models.BooleanField(verbose_name=_("Published Status"), default=False)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)

    objects= models.Manager()
    published = PropertyPublishedManager()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def save(self, *args, **kwargs):
        self.title= str.title(self.title)
        self.description= str.description(self.description)
        self.ref_code = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
        super(Property, self).save(*args, **kwargs)

    @property
    def final_property(self):
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price) + tax_amount, 2)
        return price_after_tax
    
class PropertyViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("IP Address",), max_length=250)
    property = models.ForeignKey(Property, related_name='property_views', on_delete=models.CASCADE)


    def __str__(self):
        return(

          f"Total views on a property- {self.property.title} is - {self.property.views} views(s)"
        )

    class Meta:
        verbose_name = "Total Views on Property"
        verbose_name_plural = "Total property views"







