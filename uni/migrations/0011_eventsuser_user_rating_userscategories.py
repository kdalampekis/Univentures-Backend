# Generated by Django 4.2 on 2023-05-24 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0010_categories_categ_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsuser',
            name='user_rating',
            field=models.IntegerField(default=3),
        ),
        migrations.CreateModel(
            name='UsersCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni.categories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uni.user')),
            ],
            options={
                'db_table': 'userpreferences',
                'unique_together': {('user', 'categories')},
            },
        ),
    ]
