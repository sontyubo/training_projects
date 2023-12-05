from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from .views import shopTipList, detailDelete, ShopTipDetail, ChoiceTasks, RecordView

app_name = 'shopTip'
urlpatterns = [
    path('', shopTipList.as_view(), name='index'),
    path('detail/<int:pk>/', ShopTipDetail.as_view(), name='detail'),
    path('detail/<int:pk>/delete/', detailDelete.as_view(), name='detail_delete'),
    path('choice/', ChoiceTasks.as_view(), name='choice'),
    path('record/', RecordView.as_view(), name='record'),
]