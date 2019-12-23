# Generated by Django 3.0.1 on 2019-12-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='brand name,name must be unique', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='this was when brand created')),
                ('last_modified', models.DateTimeField(auto_now_add=True, help_text='this was created when modified last')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='category name,name must be unique', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='this was created at starting')),
                ('last_modified', models.DateTimeField(auto_now_add=True, help_text='this was created whn modified last')),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CatalogueApp.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(help_text='the key of specification', max_length=250, unique=True)),
                ('vale', models.CharField(help_text='the value of specification', max_length=250, unique=True)),
                ('unit', models.CharField(help_text='the unit of specification', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='this was when brand created')),
                ('last_modified', models.DateTimeField(auto_now_add=True, help_text='this was created when modified last')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='product name,name must be unique', max_length=250, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='this was when brand created')),
                ('last_modified', models.DateTimeField(auto_now_add=True, help_text='this was created when modified last')),
                ('brand', models.ForeignKey(help_text='the brand belongs to product', on_delete=django.db.models.deletion.CASCADE, to='CatalogueApp.Brand')),
                ('category', models.ForeignKey(help_text='the category belongs to product', on_delete=django.db.models.deletion.CASCADE, to='CatalogueApp.Category')),
            ],
        ),
    ]
