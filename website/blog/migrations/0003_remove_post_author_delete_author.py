# Generated by Django 4.1.1 on 2022-09-25 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_author_alter_post_author"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="author",),
        migrations.DeleteModel(name="Author",),
    ]