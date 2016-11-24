from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='Index'),
    url(r'^comment$', views.add_comment, name='add_comment'),
    url(r'^Chip-seq$', views.Chip_seq, name='Chip_seq'),
    url(r'^Gex$', views.GeneExp_view, name='GeneExp_view'),
    url(r'^Load$', views.upload_file, name='upload_file'),
    url(r'^d3$', views.d3_data, name='d3_data'),
    url(r'^upd3$', views.d3_file_data, name='d3_file_data'),
]
