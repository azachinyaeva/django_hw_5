# Generated by Django 4.2.11 on 2024-04-19 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_scope_alter_article_options_tag_scope_article_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Тематика статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
