# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-11 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_merge_20180311_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPoster',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='board.BasePost')),
                ('title', models.CharField(max_length=128, verbose_name='제목')),
                ('title_ko', models.CharField(max_length=128, null=True, verbose_name='제목')),
                ('title_en', models.CharField(max_length=128, null=True, verbose_name='제목')),
                ('image', models.ImageField(upload_to='banner', verbose_name='이미지')),
            ],
            options={
                'verbose_name': '메인포스터',
                'verbose_name_plural': '메인포스터(들)',
            },
            bases=('board.basepost',),
        ),
        migrations.AlterModelOptions(
            name='boardbanner',
            options={'verbose_name': '게시판 배너', 'verbose_name_plural': '게시판 배너(들)'},
        ),
        migrations.AlterField(
            model_name='board',
            name='role',
            field=models.CharField(choices=[('DEFAULT', '기본'), ('PROJECT', '사업'), ('PLANBOOK', '정책자료집'), ('DEBATE', '논의'), ('ARCHIVING', '아카이빙'), ('WORKHOUR', '상근관리'), ('SPONSOR', '제휴리스트'), ('SWIPER', '격주보고'), ('STORE', '상점'), ('CONTACT', '산하기구')], default='DEFAULT', max_length=32, verbose_name='보드 역할'),
        ),
    ]