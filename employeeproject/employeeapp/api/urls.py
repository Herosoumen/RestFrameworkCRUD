from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^user/$',views.UserListCreateView.as_view(),name = 'get_create_user'),
    url(r'^user/(?P<pk>\d+)/$',views.UserUpdateView.as_view(),name = 'update_user'),
    url(r'^address/$',views.AddressListCreateView.as_view(),name = 'address_create'),
    url(r'^address/(?P<pk>\d+)/$',views.AddressUpdateView.as_view(),name = 'address_update'),
    url(r'^profile/$',views.ProfileListCreateView.as_view(),name = 'profile_create'),
    url(r'^profile/(?P<pk>\d+)/$',views.ProfileUpdateView.as_view(),name = 'profile_update'),
]
