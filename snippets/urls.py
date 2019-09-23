from django.urls import path
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from .views import UserViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view(actions={'get': 'list', 'post': 'create'})

snippet_detail = SnippetViewSet.as_view(actions={
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
    'patch': 'partial_update'
})

snippet_highlight = SnippetViewSet.as_view(actions={
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view(actions={
    'get': 'list'
})

user_detail = UserViewSet.as_view(actions={
    'get': 'retrieve'
})
urlpatterns = [
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns += [
#     path('api-auth/', include('rest_framework.urls')),
# ]
