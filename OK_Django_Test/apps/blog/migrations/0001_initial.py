# Generated by Django 2.0.5 on 2018-05-25 01:28

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('read_sum', models.IntegerField(blank=True, default=0, null=True, verbose_name='阅读数量')),
                ('like_sum', models.IntegerField(blank=True, default=0, verbose_name='点赞数')),
                ('title', models.CharField(default=None, max_length=20, verbose_name='标题')),
                ('name', models.CharField(default=None, max_length=20, verbose_name='文章题目')),
                ('theme', models.CharField(max_length=10, verbose_name='主题')),
                ('author', models.CharField(default='何泽君', max_length=5, verbose_name='作者')),
                ('write_sum', models.IntegerField(verbose_name='字数')),
                ('text', models.TextField(default=None, verbose_name='内容')),
                ('update_text', models.CharField(blank=True, max_length=50, null=True, verbose_name='更新内容')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Commets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_sum', models.IntegerField(default=0, verbose_name='评论量')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('commenter', models.CharField(max_length=20, verbose_name='评论人员')),
                ('text', models.TextField(default=None, verbose_name='内容')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Study_Sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('image', models.ImageField(default='/img/5.jpg', upload_to='img', verbose_name='上传图片')),
                ('study_tag', models.CharField(default=None, max_length=10, verbose_name='标签')),
                ('study_tag1', models.CharField(default=None, max_length=10, verbose_name='标签1')),
                ('study_tag2', models.CharField(default=None, max_length=10, verbose_name='标签2')),
                ('study_fire', models.IntegerField(default=0, verbose_name='学习热度')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='制定时间')),
                ('study_tag_select', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default=0, max_length=20, verbose_name='标签')),
            ],
            options={
                'verbose_name': '学习分类',
                'verbose_name_plural': '学习分类',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Can_reader', models.CharField(max_length=3, verbose_name='是否可以使用权限')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
