# Generated by Django 4.1.7 on 2023-03-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0007_alter_veiculo_categoria_alter_veiculo_cor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
