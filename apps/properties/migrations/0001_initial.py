# Generated by Django 4.2.2 on 2023-07-08 10:24

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Property Title"),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        always_update=True,
                        editable=False,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                (
                    "ref_code",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        unique=True,
                        verbose_name="Property Reference Code",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        default="What's unique about this property....",
                        verbose_name="Description",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        default="KE", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        default="Nairobi", max_length=180, verbose_name="City"
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(
                        default="140", max_length=100, verbose_name="Postal Code"
                    ),
                ),
                (
                    "street_address",
                    models.CharField(
                        default="Kenyatta Avenue",
                        max_length=150,
                        verbose_name="Street Address",
                    ),
                ),
                (
                    "property_number",
                    models.IntegerField(
                        default=112,
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Property Number",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Price",
                    ),
                ),
                (
                    "tax",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.15,
                        help_text="15% residential tax",
                        max_digits=8,
                        verbose_name="Property Tax",
                    ),
                ),
                (
                    "plot_area",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Property Area(meters squared)",
                    ),
                ),
                (
                    "total_floors",
                    models.IntegerField(default=0, verbose_name="Number of floors"),
                ),
                ("bedrooms", models.IntegerField(default=1, verbose_name="Bedrooms")),
                (
                    "bathrooms",
                    models.DecimalField(
                        decimal_places=2,
                        default=1.0,
                        max_digits=20,
                        verbose_name="Bathrooms",
                    ),
                ),
                (
                    "advert_type",
                    models.CharField(
                        choices=[
                            ("FOR SALE", "For sale"),
                            ("FOR RENT", "For Rent"),
                            ("AUCTION", "For Auctiom"),
                            ("AIRBNB", "Airbnb"),
                        ],
                        default="FOR SALE",
                        max_length=100,
                        verbose_name="Advert Type",
                    ),
                ),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("BUNGALOW", "Bungalow"),
                            ("COMMERCIAL", "Commercial"),
                            ("CONDOMINIUM", "Condominium"),
                            ("COTTAGE", "Cottage"),
                            ("DUPLEX", "Duplex"),
                            ("FARMHOUSE", "Farm House"),
                            ("MANSION", "Mansion"),
                            ("MOBILEHOME", "Mobile Home"),
                            ("OFFICE", "Office"),
                            ("PENTHOUSE", "Penthouse"),
                            ("STUDIO", "Studio Apartment"),
                            ("TOWNHOUSE", "Town House"),
                            ("VILLA", "Villa"),
                            ("WAREHOUSE", "Warehouse"),
                            ("OTHER", "Other"),
                        ],
                        default="MANSION",
                        max_length=50,
                        verbose_name="Property Type",
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True,
                        default="kijani.jpg",
                        null=True,
                        upload_to="",
                        verbose_name="Property Photo",
                    ),
                ),
                (
                    "photo1",
                    models.ImageField(
                        blank=True, default="interior.jpg", null=True, upload_to=""
                    ),
                ),
                (
                    "photo2",
                    models.ImageField(
                        blank=True, default="dishi.jpg", null=True, upload_to=""
                    ),
                ),
                (
                    "photo3",
                    models.ImageField(
                        blank=True, default="bedroom.jpg", null=True, upload_to=""
                    ),
                ),
                (
                    "photo4",
                    models.ImageField(
                        blank=True, default="dining.jpg", null=True, upload_to=""
                    ),
                ),
                (
                    "published_status",
                    models.BooleanField(default=False, verbose_name="Published Status"),
                ),
                ("views", models.IntegerField(default=0, verbose_name="Total Views")),
            ],
            options={
                "verbose_name": "Property",
                "verbose_name_plural": "Properties",
            },
        ),
        migrations.CreateModel(
            name="PropertyViews",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("ip", models.CharField(max_length=250, verbose_name="IP Address")),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_views",
                        to="properties.property",
                    ),
                ),
            ],
            options={
                "verbose_name": "Total Views on Property",
                "verbose_name_plural": "Total property views",
            },
        ),
    ]
