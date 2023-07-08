from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from.exceptions import NotYourProfile, ProfileNotFound
from.models import Profile
from.renderes import ProfileJSONRenderer
from.serializers import ProfileSerializer, UpdateProfileSerializer



class AgentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer

"""
    from rest_framework.decorators import api_view ,permissions

    @api_view("GET")
    @permission_classes(permission.IsAuthenticated)
    def get_user(request): 
        agent_profile= Profile.objects.filter(is_agent=True)
        serializer = Profileserializer(agent_profile, many=True)
        output = {"agent":serializer.data}
        return Response(output, status=status_HTTP_200_OK)
"""

class TopAgentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(top_agent=True)
    serializer_class =ProfileSerializer

class GetProfileApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    renderer_classes=[ProfileJSONRenderer]           

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.get(user=user)
        serializer= ProfileSerializer(user_profile, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateProfileAPIView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    renderer_classes=[ProfileJSONRenderer]  
    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user_usernamer=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        user_name= request.user.username
        if user_name != username:
            raise NotYourProfile
        data = request.data
        serializer =UpdateProfileSerializer(instance=request.user.profile, data=data, partial=True) 
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)











