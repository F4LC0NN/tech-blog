# Generated by Django 4.1.6 on 2023-02-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
    ]