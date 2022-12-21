# Generated by Django 4.1.4 on 2022-12-20 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Categoria')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('data_publicacao', models.DateField(blank=True, null=True)),
                ('edicao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Edição')),
                ('genero', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gênero textual')),
                ('editora', models.CharField(blank=True, max_length=200, null=True, verbose_name='Editora')),
                ('valor', models.DecimalField(decimal_places=2, default=99.99, max_digits=7, verbose_name='Valor')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(help_text="13 Caracteres <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>", max_length=13, unique=True, verbose_name='ISBN')),
                ('autor', models.ManyToManyField(to='primeiro_app.autor')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='primeiro_app.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
