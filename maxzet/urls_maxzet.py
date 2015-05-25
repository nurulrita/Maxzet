from django.conf.urls import patterns, include, url
from django.contrib import admin
from maxzet import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^men/$', views.MenView.as_view(), name='men'),
    url(r'^women/$', views.WomenView.as_view(), name='women'),    
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.About.as_view(), name='about'),
    url(r'^help/$', views.Help.as_view(), name='help'),

    url(r'^detail-barang-men/(?P<pk>\d+)/$', views.BarangMenDetailView.as_view(), name ='detail-barang-men'),
    url(r'^transaksi-men/(?P<id>\d+)/$', views.TransaksiMenView.as_view(id=None), name ='transaksi-men'),

    url(r'^detail-barang-women/(?P<pk>\d+)/$', views.BarangWomenDetailView.as_view(), name ='detail-barang-women'),
    url(r'^transaksi-women/(?P<id>\d+)/$', views.TransaksiWomenView.as_view(id=None), name ='transaksi-women'),

    url(r'^men/(?P<category>[\w\-]+)/$', views.MenCategoryView.as_view(), name ='men-catgory'),

)
