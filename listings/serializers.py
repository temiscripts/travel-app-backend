from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id', 'owner', 'name', 'slug', 'description',
            'location', 'price_per_night', 'is_available',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    listing_name = serializers.ReadOnlyField(source='listing.name')
    guest_email = serializers.ReadOnlyField(source='guest.email')

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_name', 'guest', 'guest_email',
            'start_date', 'end_date', 'number_of_guests', 
            'total_price', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'listing_name', 'guest_email']

