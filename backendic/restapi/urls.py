from rest_framework import routers
from restapi.views import ConfigurationViewSet, UsrsViewSet, GrpViewSet, MyGrpViewSet

router = routers.DefaultRouter()
router.register('Configuration', ConfigurationViewSet)
router.register('Usrs', UsrsViewSet)
router.register('Grp', GrpViewSet)
router.register('MyGrp', MyGrpViewSet)
