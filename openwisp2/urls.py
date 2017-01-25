from django.conf.urls import include, url
from organizations.backends import invitation_backend

urlpatterns = [
    # organizations
    url(r'^accounts/', include('organizations.urls')),
    url(r'^invitations/', include(invitation_backend().get_urls())),
    # django-netjsonconfig schemas
    url(r'^', include('django_netjsonconfig.urls', namespace='netjsonconfig')),
    # openwisp2.pki (CRL view)
    url(r'^', include('openwisp2.pki.urls', namespace='x509')),
    # controller
    url(r'^', include('openwisp2.config.controller.urls', namespace='controller')),
    # openwisp2.ui
    url(r'', include('openwisp2.ui.urls', namespace='ui', app_name='ui')),
]
