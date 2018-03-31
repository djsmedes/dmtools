"""dmtools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from base.views import HomepageView, update_effect_list, remove_effect

breadcrumbs = [
    {'href': '/', 'text': 'Home'},
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(extra_context={'breadcrumbs': breadcrumbs}), name='home'),
    path('', include('people.urls')),
    path('', include('statblocks.urls')),
    path('places/', include('places.urls')),
    path('plot/', include('plot.urls')),
    path('ajax/update-effect-list/', update_effect_list, name='ajax-update-effect-list'),
    path('ajax/remove-effect/', remove_effect, name='ajax-remove-effect'),
]
