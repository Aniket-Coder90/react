from cafe.models import Menu, QRTable, Restaurant, order
from rest_framework import serializers

class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:

        model = Restaurant
        fields = ('name','key')

class QRTableSerializer(serializers.ModelSerializer):

    class Meta:

        model = QRTable
        fields = ('link', 'table_id', 'restaurant')

class MenuSerializer(serializers.ModelSerializer):

    class Meta:

        model = Menu
        fields = ('sr_no', 'restaurant', 'category', 'item', 'item_desc', 'item_image')

class orderSerializer(serializers.ModelSerializer):

    class Meta:

        model = order
        fields = ('order_id', 'rest_name', 'rest_table_id', 'order_item', 'order_total', 'order_date_time', 'payment_options')
