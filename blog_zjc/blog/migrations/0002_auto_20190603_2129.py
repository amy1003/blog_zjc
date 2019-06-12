# Generated by Django 2.0.3 on 2019-06-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-create_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AddField(
            model_name='post',
            name='views_num',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]
