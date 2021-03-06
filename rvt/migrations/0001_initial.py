# Generated by Django 3.0.2 on 2021-02-13 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RVTvPartition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vi_batch', models.IntegerField(null=True)),
                ('rvt_vp_vmid', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vp_disk', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vp_capacitymb', models.IntegerField(null=True)),
                ('rvt_vp_consumedmb', models.IntegerField(null=True)),
                ('rvt_vp_freemb', models.IntegerField(null=True)),
                ('rvt_vp_annotation', models.CharField(default='UNSET', max_length=300)),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('rvt_vp_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vp_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RVTvInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vi_batch', models.IntegerField(null=True)),
                ('rvt_vi_filename_orig', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_vm', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vi_powerstate', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_dnsname', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vi_cpus', models.IntegerField(null=True)),
                ('rvt_vi_memory', models.IntegerField(null=True)),
                ('rvt_vi_nics', models.IntegerField(null=True)),
                ('rvt_vi_disks', models.IntegerField(null=True)),
                ('rvt_vi_rsrcpool', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_folder', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_provisioned_mb', models.IntegerField(null=True)),
                ('rvt_vi_in_use_mb', models.IntegerField(null=True)),
                ('rvt_vi_unshared_mb', models.IntegerField(null=True)),
                ('rvt_vi_hwversion', models.IntegerField(null=True)),
                ('rvt_vi_path', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_datacenter', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_cluster', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_host', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_os_config', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_os_vmtools', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vi_id', models.CharField(blank=True, default='UNSET', max_length=300, null=True)),
                ('rvt_vi_uuid', models.CharField(blank=True, default='UNSET', max_length=300, null=True)),
                ('rvt_vi_sdkserver', models.CharField(blank=True, default='UNSET', max_length=300, null=True)),
                ('rvt_vi_sdks_type', models.CharField(blank=True, default='UNSET', max_length=300, null=True)),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('rvt_vi_assessment', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vi_assessment', to='org.Assessment')),
                ('rvt_vi_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vi_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RVTvHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vi_batch', models.IntegerField(null=True)),
                ('rvt_vh_hostname', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vh_datacenter', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vh_cluster', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vh_cputype', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vh_speed', models.IntegerField(null=True)),
                ('rvt_vh_socketcount', models.IntegerField(null=True)),
                ('rvt_vh_socketcores', models.IntegerField(null=True)),
                ('rvt_vh_cores', models.IntegerField(null=True)),
                ('rvt_vh_cpu_usagepercent', models.IntegerField(null=True)),
                ('rvt_vh_memorymb', models.IntegerField(null=True)),
                ('rvt_vh_mem_usagepercent', models.IntegerField(null=True)),
                ('rvt_vh_vmcount', models.IntegerField(null=True)),
                ('rvt_vh_vmpercore', models.IntegerField(null=True)),
                ('rvt_vh_vcpucount', models.IntegerField(null=True)),
                ('rvt_vh_vcpupercore', models.IntegerField(null=True)),
                ('rvt_vh_vram', models.IntegerField(null=True)),
                ('rvt_vh_usedmem', models.IntegerField(null=True)),
                ('rvt_vh_swapmem', models.IntegerField(null=True)),
                ('rvt_vh_balloonmem', models.IntegerField(null=True)),
                ('rvt_vh_evc', models.CharField(blank=True, max_length=100, null=True)),
                ('rvt_vh_maxevc', models.CharField(blank=True, max_length=100, null=True)),
                ('rvt_vh_esxversion', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vh_boottime', models.CharField(blank=True, max_length=300, null=True)),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('rvt_vh_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vh_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RVTvDisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vi_batch', models.IntegerField(null=True)),
                ('rvt_vd_vmid', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vd_disk', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vd_capacitymb', models.IntegerField(null=True)),
                ('rvt_vd_diskmode', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vd_thin', models.BooleanField(default=False)),
                ('rvt_vd_controller', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vd_path', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vd_annotation', models.CharField(default='UNSET', max_length=300)),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('rvt_vd_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vd_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RVTvDatastore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rvt_vi_batch', models.IntegerField(null=True)),
                ('rvt_vs_name', models.CharField(blank=True, max_length=300, null=True)),
                ('rvt_vs_type', models.CharField(default='UNSET', max_length=300)),
                ('rvt_vs_vmcount', models.IntegerField(null=True)),
                ('rvt_vs_capacitymb', models.IntegerField(null=True)),
                ('rvt_vs_provisionedmb', models.IntegerField(null=True)),
                ('rvt_vs_usedmb', models.IntegerField(null=True)),
                ('rvt_vs_freemb', models.IntegerField(null=True)),
                ('load_time', models.DateTimeField(auto_now_add=True)),
                ('last_edit', models.DateTimeField(auto_now=True)),
                ('rvt_vs_user', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='rvt_vs_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
