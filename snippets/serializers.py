from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# 장고의 form과 유사하게 작동하는 serializer 선언
# 즉, required, max_length, default 처럼 다양한 필드에 유사한 유효성 검사 플래그를 포함

class SnippetSerializer(serializers.Serializer):
    # serializer/deserializer 되는 필드를 정의
    # 필드 플래그는 또한 HTML로 렌더링 할때 처럼 특정한 상황에서 serializer가 표시되는 방식을 제어할 수 있음
    # 검색 가능한 API가 표시되어지는 방식을 제어하는데 특히 유용
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # 메서드는 serializer.save() 호출 시에 완전한 인스턴스가 생성되거나 수정
    def create(self, validated_data):
        """
        유효한 데이터가 들어오면 Snippet 인스턴스를 만들고 반환함
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        유효한 데이터가 들어오면 Snippet 인스턴스를 업데이트하고 반환함
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']