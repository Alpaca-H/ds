# Generated by Django 2.0.5 on 2018-05-25 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180525_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study_sort',
            name='study_tag_select',
            field=models.CharField(choices=[('web开发', 'web开发'), ('网络安全', '网络安全'), ('爬虫', '爬虫'), ('自然语言处理', '自然语言处理')], default=0, max_length=20, verbose_name='标签'),
        ),
    ]
