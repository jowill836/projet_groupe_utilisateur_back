from rest_framework import serializers
from restapi.models import Configuration, Usrs, Grp

class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = '__all__'

class UsrsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usrs
        fields = '__all__'

class GrpSerializer(serializers.ModelSerializer):
    nbUser = serializers.SerializerMethodField()

    class Meta:
        model = Grp
        fields = '__all__'
    def get_nbUser(self, obj):
        return Usrs.objects.filter(grp_id=obj.grp_id).count()

