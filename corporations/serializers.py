from corporations.models import Recruitment
from rest_framework import serializers

class AllRecruitmentSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    corporation = serializers.SerializerMethodField()
    position_name = serializers.SerializerMethodField()
    tech_stack_name = serializers.SerializerMethodField()
    
    def get_country(self, obj):
        return obj.corporation.country.name  

    def get_region(self, obj):
        return obj.corporation.region.name  
    
    def get_corporation(self, obj):
        return obj.corporation.name
    
    def get_position_name(self, obj):
        return obj.position.name
    
    def get_tech_stack_name(self, obj):
        return obj.tech_stack.name
    
    class Meta:
        model = Recruitment
        fields = ['id', 'corporation', 'country', 'region', 'position', 'position_name', 'tech_stack', 'tech_stack_name','recompense', 'content']
        
        extra_kwargs = {
            'position': {'write_only': True},
            'tech_stack': {'write_only': True},
        }
        
class RecruitmentSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField()
    tech_stack_name = serializers.SerializerMethodField()

    def get_position_name(self, obj):
        return obj.position.name
    
    def get_tech_stack_name(self, obj):
        return obj.tech_stack.name
    
    class Meta:
        model = Recruitment
        fields = ['corporation', 'position', 'position_name', 'recompense', 'content', 'tech_stack', 'tech_stack_name', ]
        
        extra_kwargs = {
            'position': {'write_only': True},
            'tech_stack': {'write_only': True},
        }
        
class PutRecruitmentSerializer(serializers.ModelSerializer):
    position_name = serializers.SerializerMethodField()
    tech_stack_name = serializers.SerializerMethodField()
    
    def get_position_name(self, obj):
        return obj.position.name
    
    def get_tech_stack_name(self, obj):
        return obj.tech_stack.name
    
    class Meta:
        model = Recruitment
        fields = ['position', 'position_name', 'recompense', 'content', 'tech_stack', 'tech_stack_name']
        
        extra_kwargs = {
            'position': {'write_only': True},
            'tech_stack': {'write_only': True},
        }