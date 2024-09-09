from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from .views import UserViewSet, TodoViewSet

router = SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'todos', TodoViewSet)

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'todos', TodoViewSet, basename='user-todos')
