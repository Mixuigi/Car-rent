from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from KursRabota.views import register  # SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('KursRabota.urls')),
    #url(r'^KursRabota/', include(('KursRabota.urls', 'KursRabota'),
                                # namespace='KursRabota', ), )

]


