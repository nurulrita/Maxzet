from django.conf.urls import patterns, include, url
from django.contrib import admin
from maxzet import urls_maxzet
from maxzet.views import HomeView as home
urlpatterns = patterns('',
    # Examples:

    url(r'^$', home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^maxzet/', include(urls_maxzet)),

)	
