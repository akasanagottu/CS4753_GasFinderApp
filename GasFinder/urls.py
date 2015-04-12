from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GasApplication.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', 'GasFinder.views.home', name='home'),
    url(r'^register/$', 'GasFinder.views.register', name='register'),
    url(r'^submit_price/$', 'GasFinder.views.submit_price', name='submit_price'),
    url(r'^search/$', 'GasFinder.views.search', name='search'),
    url(r'^search_local/$', 'GasFinder.views.search_local', name='search_local'),
    url(r'^$', 'GasFinder.views.user_login', name='main_page'),
    url(r'^forgot_account/$', 'GasFinder.views.forgot_account', name='forgot_account'),
    url(r'^advertise/$', 'GasFinder.views.advertise', name='advertise'),
    url(r'^account/$', 'GasFinder.views.account', name='account'),
    url(r'^about/$', 'GasFinder.views.about', name='about'),
    url(r'^logout/$', 'GasFinder.views.user_logout', name='logout'),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
