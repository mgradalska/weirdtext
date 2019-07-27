from django.urls import path

from app.views import DecodeView, EncodeView

urlpatterns = [
    path('decode/', DecodeView.as_view(), name='decode'),
    path('encode/', EncodeView.as_view(), name='encode')
]
