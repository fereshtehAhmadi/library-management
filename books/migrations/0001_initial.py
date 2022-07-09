# Generated by Django 4.0.6 on 2022-07-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Authorrr',
                'verbose_name_plural': 'Authorss',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Publishers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('translator', models.CharField(blank=True, max_length=50, null=True)),
                ('publisher', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('translator', models.CharField(max_length=100)),
                ('condition', models.BooleanField(default=True)),
                ('author', models.ManyToManyField(to='books.author')),
                ('category', models.ManyToManyField(to='books.categorie')),
                ('publishers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.publishers')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='accounts.customusermodel')),
            ],
        ),
    ]
