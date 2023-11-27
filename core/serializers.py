from rest_framework import serializers

#convert djongo models into json for response
class ImgLinkSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=200)


class ChordImagesSerializer(serializers.Serializer):
    chord_name = serializers.CharField(max_length=10)
    images = ImgLinkSerializer(many=True)

    def to_representation(self, instance):
        # needed for djongo array field
        representation = super().to_representation(instance)
        representation['images'] = [{'link': img['link']} for img in representation['images']]
        return representation