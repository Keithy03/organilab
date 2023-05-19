import logging

from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from laboratory.api.serializers import BaseShelfObjectSerializer
from laboratory.models import Laboratory, ShelfObject

logger = logging.getLogger('organilab')


class AddShelfObjectSerializer(serializers.Serializer):
    amount = serializers.FloatField()
    bill = serializers.CharField(required=False)
    provider = serializers.IntegerField(required=False)
    shelf_object = serializers.IntegerField()


class SubstractShelfObjectSerializer(serializers.Serializer):
    discount = serializers.FloatField()
    description = serializers.CharField(required=False)
    shelf_object = serializers.IntegerField()


class TransferOutShelfObjectSerializer(serializers.Serializer):
    shelf_object = serializers.PrimaryKeyRelatedField(queryset=ShelfObject.objects.all())
    amount_to_transfer = serializers.FloatField(min_value=0.1)
    mark_as_discard = serializers.BooleanField(default=False)
    laboratory = serializers.PrimaryKeyRelatedField(queryset=Laboratory.objects.all())
    
    def validate_shelf_object(self, value):
        attr = super().validate(value)
        source_laboratory_id = self.context.get("source_laboratory_id")
        if attr.in_where_laboratory_id != source_laboratory_id:
            logger.debug(f'TransferOutShelfObjectSerializer --> attr.in_where_laboratory_id '
                         f'({attr.in_where_laboratory_id}) != source_laboratory_id ({source_laboratory_id})') 
            raise serializers.ValidationError(_("Object does not exist in the laboratory"))
        return attr


class ShelfObjectDeleteSerializer(serializers.Serializer):
    shelfobj = serializers.PrimaryKeyRelatedField(queryset=ShelfObject.objects.all())

    def validate_shelfobj(self, value):
        attr = super().validate(value)
        if attr.in_where_laboratory_id != self.context.get('laboratory_id'):
            logger.debug(f'ShelfObjectDeleteSerializer --> attr.in_where_laboratory_id ({attr.in_where_laboratory_id}) '
                         f'!= laboratory_id ({self.context.get("laboratory_id")})')
            raise serializers.ValidationError(_("Object does not exist in the laboratory"))
        return attr


class ShelfObjectDetailSerializer(BaseShelfObjectSerializer, serializers.ModelSerializer):
    object_detail = serializers.SerializerMethodField()
    object_name = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    object_inst = serializers.SerializerMethodField()
    object_features = serializers.SerializerMethodField(required=False, allow_null=True)

    class Meta:
        model = ShelfObject
        fields = '__all__'

    def get_object_detail(self, obj):
        return obj.get_object_detail()

    def get_object_features(self, obj):
        if obj.object.features.exists():
            return obj.object.features.all()

    def get_object_inst(self, obj):
        return obj.object