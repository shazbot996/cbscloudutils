from django.contrib import admin

from .models import RVTvInfo, RVTvDisk, RVTvPartition, RVTvDatastore, RVTvHost

admin.site.register(RVTvInfo)
admin.site.register(RVTvDisk)
admin.site.register(RVTvPartition)
admin.site.register(RVTvDatastore)
admin.site.register(RVTvHost)
