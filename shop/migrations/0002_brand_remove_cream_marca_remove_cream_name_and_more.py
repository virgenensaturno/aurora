# Generated by Django 4.0.2 on 2022-11-25 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('raiting', models.PositiveBigIntegerField(choices=[(1, 'Muy mala'), (2, 'Mala'), (3, 'Buena'), (4, 'Muy Buena'), (5, 'Exelente')], default=1)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='cream',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='cream',
            name='name',
        ),
        migrations.RemoveField(
            model_name='cream',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='cream',
            name='types',
        ),
        migrations.RemoveField(
            model_name='type',
            name='name',
        ),
        migrations.AddField(
            model_name='cream',
            name='raiting',
            field=models.PositiveBigIntegerField(default=1, verbose_name=[(1, 'Muy mala'), (2, 'Mala'), (3, 'Buena'), (4, 'Muy Buena'), (5, 'Exelente')]),
        ),
        migrations.AddField(
            model_name='cream',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='cream',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.type'),
        ),
        migrations.AddField(
            model_name='type',
            name='description',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='type',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='cream',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cream',
            name='description',
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cream',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cover'),
        ),
        migrations.AlterField(
            model_name='cream',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.AddField(
            model_name='cream',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.brand'),
        ),
    ]
