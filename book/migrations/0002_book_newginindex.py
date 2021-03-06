# Generated by Django 3.2.6 on 2021-08-24 18:05

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            [
                "CREATE EXTENSION IF NOT EXISTS pg_trgm;",
                "UPDATE pg_opclass SET opcdefault = true WHERE opcname='gin_trgm_ops';",
            ]
        ),
        migrations.AddIndex(
            model_name="book",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["title"], name="NewGinIndex", opclasses=["gin_trgm_ops"]
            ),
        ),
    ]
