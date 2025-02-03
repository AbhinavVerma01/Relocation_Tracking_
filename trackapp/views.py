from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import tracker
from .serializers import trackerSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view



# class trackerViewSet(viewsets.ModelViewSet):
#     queryset = tracker.objects.all()
#   serializer_class = trackerSerializer serializer_class = trackerSerializer


@api_view(['POST'])
def post_tracker(request):
    #for POST request
    if request.method == 'POST':
        serializer = trackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def request_tracker(request, pk=None):
    # for GET request
    if request.method == 'GET':
        if pk:
            tracker_obj = get_object_or_404(tracker, pk=pk)
            serializer = trackerSerializer(tracker_obj)
        else:
            trackers = tracker.objects.all()
            serializer = trackerSerializer(trackers, many=True)
        return Response(serializer.data)

    # for PUT request
    elif request.method == 'PUT':
        tracker_obj = get_object_or_404(tracker, pk=pk)
        serializer = trackerSerializer(tracker_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#for DELETE request
    elif request.method == 'DELETE':
        tracker_obj = get_object_or_404(tracker, pk=pk)
        tracker_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
serializer_class = trackerSerializer













# # class based -----------------------
# class trackerView(APIView):
#     serializer_class = trackerSerializer

#     def post(self, request):
#         serializer = trackerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 tracker_obj = tracker.objects.get(pk=pk)
#                 serializer = trackerSerializer(tracker_obj)
#             except tracker.DoesNotExist:
#                 raise Http404("No Data found ")
#         else:
#             trackers = tracker.objects.all()
#             serializer = trackerSerializer(trackers, many=True)
#         return Response(serializer.data)
    

#     def put(self, request, pk):
#         try:
#             tracker_obj = tracker.objects.get(pk=pk)
#         except tracker.DoesNotExist:
#             return Response({"error":" Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = trackerSerializer(tracker_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         try:
#             tracker_obj = tracker.objects.get(pk=pk)
#         except tracker.DoesNotExist:
#             return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         tracker_obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
