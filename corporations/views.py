from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from corporations.models import Recruitment

from corporations.serializers import (
    AllRecruitmentSerializer,
    RecruitmentSerializer,
    PutRecruitmentSerializer
    )

class SearchView(APIView):
    """
    채용공고 검색
    """
    def get(self, request):
        data_for_search = str(self.request.query_params.get('search'))

        searched_data = (
            Recruitment.objects.filter(corporation__name__icontains=data_for_search)
            |Recruitment.objects.filter(content__icontains=data_for_search)
            |Recruitment.objects.filter(tech_stack__name__icontains=data_for_search)
            )

        searched_job_post_serializer_data = AllRecruitmentSerializer(searched_data, many=True).data
        return Response(searched_job_post_serializer_data)
    
class RecruitmentView(APIView):
    """
    채용공고 전체목록 조회, 등록, 수정, 삭제
    """
    def get(self, request):
        recruitments = Recruitment.objects.all()
        serialized_data = AllRecruitmentSerializer(recruitments, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
        
    def post(self, request):
        data = {
            'corporation' : request.data['corporation'],
            'position' : request.data['position'],
            'tech_stack' : request.data['tech_stack'],
            'recompense' : request.data['recompense'],
            'content' : request.data['content'],
        }

        serializer = RecruitmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, recruitment_id):
        try:
            recruitment = Recruitment.objects.get(id=recruitment_id)  

        except Recruitment.DoesNotExist:
            return Response({'message' : '해당 공고가 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)
                  
        serializer = PutRecruitmentSerializer(recruitment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, recruitment_id):
        try:
            recruitment = Recruitment.objects.get(id=recruitment_id)  
            recruitment.delete()
            return Response({'message' : '해당 공고가 삭제되었습니다'}, status=status.HTTP_200_OK)

        except Recruitment.DoesNotExist:
            return Response({'message' : '해당 공고가 존재하지 않습니다'}, status=status.HTTP_404_NOT_FOUND)

class RecruitmentDetailView(APIView):
    """
    채용공고 상세페이지
    """
    def get(self, request, recruitment_id):
        recruitment = Recruitment.objects.get(id=recruitment_id)
        serialized_data = AllRecruitmentSerializer(recruitment).data
        return Response(serialized_data, status=status.HTTP_200_OK)
        