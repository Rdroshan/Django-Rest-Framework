from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         '''
#         create and return a new 'Snippet'instance, given the validated data
#         :param validated_data:
#         :return:
#         '''
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validate_data):
#         """
#         Update and return an existing 'Snippet' instance, given the validated data.
#         :param instance:
#         :param validate_data:
#         :return:
#         """
#         instance.title = validate_data.get('title', instance.title)
#         instance.code = validate_data.get('code', instance.code)
#         instance.linenos = validate_data.get('linenos', instance.linenos)
#         instance.language = validate_data.get('language', instance.language)
#         instance.style = validate_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializer(serializers.ModelSerializer):
    """
    ReadOnlyField is untyped field, that means it is readonly and will only be used for serializer
    representations, but will not be used for updating model instances when they are deserialized.
    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        """
        Because snippets is a reverse relation on User model, it will not be included by default when 
        using ModelSerializer.
        """
        fields = ['id', 'username', 'snippets']
