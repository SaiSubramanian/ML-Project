from django.conf.urls import url
from CA_PgMP import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^Predict', views.processPrediction, name='UI')
]
