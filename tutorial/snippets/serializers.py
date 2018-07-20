from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelated(many=True, query=Snippet.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets','owner')