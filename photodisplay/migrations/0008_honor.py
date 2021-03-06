# Generated by Django 2.2.2 on 2019-07-27 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photodisplay', '0007_auto_20190702_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Honor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名字')),
                ('content', models.TextField(verbose_name='正文内容')),
                ('status', models.PositiveIntegerField(choices=[(1, '显示'), (0, '不显示')], default=1, verbose_name='展示状态')),
                ('info_catogory', models.PositiveIntegerField(choices=[(2, '主页超长介绍'), (1, '主页中间短事迹描述'), (0, '荣誉')], default=1, verbose_name='分类')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '主页文字信息',
                'verbose_name_plural': '主页文字信息',
            },
        ),
    ]
