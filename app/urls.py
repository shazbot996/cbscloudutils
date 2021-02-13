"""URL Configuration
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView

from .views import index, me, initadmin

urlpatterns = [
    url(r'^favicon\.ico$',RedirectView.as_view(url=settings.STATIC_URL + 'favicon.ico')),
    url(r'^$', index, name="app_index"),
    url(r'^me$',
        me,
        name="user_home"),
    url('login$',
        LoginView.as_view(template_name="app/app_login_form.html"),
        name="user_login"),
    url(r'logout$',
        LogoutView.as_view(),
        name="user_logout"),

    url(r'^admin/', admin.site.urls),
    url('^initadmin/', initadmin),

    url('^autobrik/', include('autobrik.urls')),
    url('^rvt/', include('rvt.urls')),
    url('^org/', include('org.urls')),
    url('^fusioncharts/', include('org.urls')),


    # EXAMPLE PARAMETER PASS
    # url(r'id_lookup/(?P<id>\d+)/$',
    #     id_lookup, name="module_id_lookup")
    #
    # THIS CAN BE REFERENCED IN HTML ALSO BY THIS:
    #
    # <a href="{% url 'module_id_lookup' id=module.id %}">

]
