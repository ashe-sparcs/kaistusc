# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-15 17:38
from __future__ import unicode_literals

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='번호')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='제목')),
            ],
            options={
                'verbose_name': '조',
                'verbose_name_plural': '조(들)',
                'ordering': ['num'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_type', models.CharField(choices=[('PRE', '전문'), ('CHAP', '장'), ('SEC', '절'), ('SUPPL', '부칙')], max_length=8, verbose_name='종류')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='번호')),
                ('content', models.CharField(max_length=128, verbose_name='내용')),
                ('parent_chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_chapters', to='rule.Chapter', verbose_name='상위챕터')),
                ('prev_chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_chapters', to='rule.Chapter', verbose_name='직전연혁')),
            ],
            options={
                'verbose_name': '장/절',
                'verbose_name_plural': '장/절(들)',
            },
        ),
        migrations.CreateModel(
            name='Clause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='번호')),
                ('content', models.TextField(verbose_name='내용')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='rule.Article', verbose_name='조')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='rule.Chapter', verbose_name='챕터')),
            ],
            options={
                'verbose_name': '항',
                'verbose_name_plural': '항(들)',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True, verbose_name='내용')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='최종 수정일')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '논의댓글',
                'verbose_name_plural': '논의댓글(들)',
            },
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_committee', models.BooleanField(default=False, verbose_name='위원회 논의여부')),
                ('subject', models.CharField(max_length=64, verbose_name='주제')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='최종 수정일')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussions', to='rule.Article', verbose_name='조항')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussions', to='rule.Chapter', verbose_name='챕터')),
            ],
            options={
                'verbose_name': '논의사항',
                'verbose_name_plural': '논의사항(들)',
                'ordering': ['-from_committee'],
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='규정명')),
                ('rule_type', models.CharField(choices=[('CONST', '회칙'), ('BYLAW', '세칙'), ('RULE', '규칙'), ('ETC', '기타규정')], max_length=8, verbose_name='종류')),
                ('revision_type', models.CharField(choices=[('ESTAB', '제정'), ('PART', '일부개정'), ('FULL', '전부개정')], max_length=8, verbose_name='제개정 종류')),
                ('date_resolved', models.DateField(blank=True, null=True, verbose_name='의결일')),
            ],
            options={
                'verbose_name': '규정',
                'verbose_name_plural': '규정(들)',
                'ordering': ['-date_resolved'],
            },
        ),
        migrations.CreateModel(
            name='RuleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=16, verbose_name='축약 영문구')),
                ('is_main', models.BooleanField(default=False, verbose_name='기본 규정여부')),
            ],
            options={
                'verbose_name': '규정세트',
                'verbose_name_plural': '규정세트(들)',
            },
        ),
        migrations.AddField(
            model_name='rule',
            name='rule_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='rule.RuleSet', verbose_name='규정세트'),
        ),
        migrations.AddField(
            model_name='discussion',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='discussions', to='rule.Rule', verbose_name='규정'),
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='rule.Discussion', verbose_name='논의'),
        ),
        migrations.AddField(
            model_name='clause',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clauses', to='rule.Rule', verbose_name='규정'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='rule.Rule', verbose_name='규정'),
        ),
        migrations.AddField(
            model_name='article',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='rule.Chapter', verbose_name='챕터'),
        ),
        migrations.AddField(
            model_name='article',
            name='prev_article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_article', to='rule.Article', verbose_name='직전연혁'),
        ),
        migrations.AddField(
            model_name='article',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='rule.Rule', verbose_name='규정'),
        ),
    ]
