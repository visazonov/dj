from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from crud_demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']       # поля которые хотим отображать

    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('Вы использовали запрещенное слово - Текст ')
        return value

    # def validate(self, attrs):
    #     if 'hello' in attrs['text'] or attrs['user'].id == 1:
    #         raise ValidationError('Что-то пошло не так')
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

