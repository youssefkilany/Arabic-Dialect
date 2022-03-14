from django.urls import path, include, re_path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landingPage, name='recognitionServiceLanding'),
    path('DialectRecognizer', views.landingPage, name='recognitionServiceLanding'),
    path('DialectRecognizer/', views.landingPage, name='recognitionServiceLanding'),

    # (?P<model>(?i)([m|d]l)$)
    # (?P ) match pattern; <model> pass this match as variable named model to View function
    # (?i) match is case insensitive; ([m|d]l) character m or d followed by l, all case insensitive
    # $ end of path, means that if there's anything following ml/dl, this isn't a proper url
    re_path('DialectRecognizer/(?P<model>(?i)([m|d]l)$)', views.DialectRecognizer, name='model'),
    # path('DialectRecognizer/ML', views.DialectRecognizerML, name='mlmodel'),
    # path('DialectRecognizer/dl', views.DialectRecognizerDL, name='dlmodel')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
