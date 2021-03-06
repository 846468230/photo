# Generated by Django 2.2.2 on 2019-06-28 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=100, verbose_name='评论目标')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese_name', models.CharField(default='', max_length=128, verbose_name='中文名')),
                ('school', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='学校')),
                ('college', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='学院')),
                ('major', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='专业')),
                ('phone', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='电话')),
                ('qq', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='qq')),
                ('wechat', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='微信')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('content', models.TextField(help_text='正文必须为MarkDown格式', verbose_name='正文')),
                ('content_html', models.TextField(blank=True, editable=False, verbose_name='正文html代码')),
                ('camera', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='相机及型号')),
                ('focus', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='对焦参数')),
                ('aperture', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='光圈参数')),
                ('shutter_time', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='快门时间')),
                ('sensitive', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='感光参数')),
                ('status', models.PositiveIntegerField(choices=[(1, '主页显示'), (2, '分类页面显示'), (0, '不显示')], default=1, verbose_name='展示状态')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photodisplay.Category', verbose_name='分类')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
            },
        ),
    ]
