from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model =Book
        fields="__all__"

    def validate(self, attrs):
        title=attrs.get('title',None)
        price=attrs.get('price',None)
        isbt=attrs.get('isbt',None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":"False",
                    "message":"Siz titlega son kiritib yubordingiz"
                }
            )
        if Book.objects.filter(title=title,isbt=isbt):
            raise ValidationError(
                {
                    "status":"False",
                    "message":"Bu kitob bor"
                }
            )

        if Book.objects.filter(isbt=isbt):
            raise ValidationError(
                {
                    "status":"False",
                    "message":"isbt ro'yxatdan o'tgan"
                }
            )


        return attrs

    def validate_price(self, price):
        if price<0:
            raise ValidationError(
                {
                    "status":"False",
                    "message":"narxni xato kiritingiz"
                }
            )