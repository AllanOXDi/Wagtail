# Generated by Django 4.1.1 on 2022-09-12 17:08

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0076_modellogentry_revision"),
        ("wagtailimages", "0024_index_image_file_hash"),
        ("home", "0003_homepage_banner_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="banner_cta",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_subtitle",
            field=wagtail.fields.RichTextField(default="test"),
            preserve_default=False,
        ),
    ]
