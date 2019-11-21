# Generated by Django 2.1.14 on 2019-11-20 19:12

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
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('F', 'First Player to Move'), ('S', 'Second Player to Move'), ('W', 'First Player Wins'), ('L', 'Second Player Wins'), ('D', 'Draw')], default='F', max_length=1)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_first_player', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(blank=True, max_length=300)),
                ('by_first_player', models.BooleanField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autobrik.Game')),
            ],
        ),
        migrations.CreateModel(
            name='VMdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vm', models.CharField(blank=True, max_length=300, verbose_name='VM Name')),
                ('rvt_powerstate', models.CharField(blank=True, help_text='TESTING', max_length=300, verbose_name='Power State')),
                ('rvt_guest_state', models.CharField(blank=True, max_length=300, verbose_name='Guest OS State')),
                ('rvt_provisioned_mb', models.IntegerField(null=True)),
                ('rvt_in_use_mb', models.IntegerField(null=True)),
                ('rvt_unshared_mb', models.IntegerField(null=True)),
                ('rvt_user', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
