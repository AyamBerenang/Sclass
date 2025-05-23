# Generated by Django 5.1.7 on 2025-05-09 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_todolist', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                ("""
                    CREATE TABLE todolist_post (
                        id serial primary key,
                        task_name varchar(255) NOT NULL,
                        task_desc text NOT NULL,
                        task_deadline date NOT NULL,
                        created_at date default now()
                    );
                """)
            ], 

            reverse_sql=[
                ("""
                    drop table if exists todolist_post;
                """)
            ])
    ]
