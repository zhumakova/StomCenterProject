from django.urls import path
from .views import *

urlpatterns = [
    path('',DayViewSet.as_view({
        'get':'list',
        'post':'create'
                                }), name='day'),
    path('day/<int:day_id>/',DayViewSet.as_view(
        {
            'get':'retrieve',
            'put':'update',
            'delete':'destroy',
        }), name='day_detail'),
    path('doctor_day/',DoctorDayView.as_view({
        'get':'list'
    }),name='doctor_day'),
    path('create_wd/<int:day_id>/',DoctorDayView.as_view({
        'post':'create'
    }),name='create_wd'),
    path('modify_wd/<int:doctor_day_id>/',DoctorDayView.as_view({
        'put':'update',
        'get':'retrieve',
    }),name='modify_wd'),
    path('order/',OrderViewSet.as_view({
        'get':'list',
        'post':'create',
    }),name='order'),
    path('order/<int:order_id>/',OrderViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }
    )),
    path('doctors/',DoctorViewSet.as_view({
        'get':'list'
    })),
    path('doctors/<str:d_username>/',DoctorViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    }))


]