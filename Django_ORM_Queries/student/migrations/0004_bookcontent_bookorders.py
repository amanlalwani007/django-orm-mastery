# Generated by Django 3.1 on 2022-08-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_books_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookOrders',
            fields=[
            ],
            options={
                'ordering': ['created'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('student.bookcontent',),
        ),
    ]