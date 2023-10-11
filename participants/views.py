from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import * 
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView

from .models import Participant
from .serializers import ParticipantSerializer
 
def convertStringToSeconds(time):
    if ":" in time:
        min_sec = time.split(":")
        result = float(min_sec[0]) * 60 + float(min_sec[1])
        return result
    else:
        return float(time)

@api_view()
def home(request):
    return Response('''Home Page  try:  cubing/participants/''')

class ParticipantList(ListCreateAPIView):
    queryset = Participant.objects.all().order_by("solve_best")
    serializer_class = ParticipantSerializer

    def post(self, request):
        solve1 = convertStringToSeconds(request.data['solve1'])
        solve2 = convertStringToSeconds(request.data['solve2'])
        solve3 = convertStringToSeconds(request.data['solve3'])
        solve4 = convertStringToSeconds(request.data['solve4'])
        solve5 = convertStringToSeconds(request.data['solve5'])
        solves = [solve1, solve2, solve3, solve4, solve5]
        solves.sort()
        solve_avg =  "{:.3f}".format((solves[1] + solves[2] + solves[3])/3)
        solve_best = min(solves)
        result_data = {
            "student_id": request.data['student_id'],
            "name":request.data['name'], 
            "competetion":request.data['competetion'],
            "solve1":solve1,
            "solve2":solve2,
            "solve3":solve3,
            "solve4":solve4,
            "solve5":solve5,
            "solve_best":solve_best,
            "solve_avg":solve_avg
        }

        serializer = ParticipantSerializer(data= result_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ParticipantListAvg(ListAPIView):
    queryset = Participant.objects.all().order_by("solve_avg")
    serializer_class = ParticipantSerializer


class ParticipantDetail(RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def update(self, request, pk):
        participant = get_object_or_404(Participant, pk=pk)

        solve1 = convertStringToSeconds(request.data['solve1'])
        solve2 = convertStringToSeconds(request.data['solve2'])
        solve3 = convertStringToSeconds(request.data['solve3'])
        solve4 = convertStringToSeconds(request.data['solve4'])
        solve5 = convertStringToSeconds(request.data['solve5'])
        solves = [solve1, solve2, solve3, solve4, solve5]
        solves.sort()
        solve_avg =  "{:.3f}".format((solves[1] + solves[2] + solves[3])/3)
        solve_best = min(solves)
        if min(float(participant.solve_avg), float(solve_avg)) == solve_avg:
            result_data = {
                "student_id": request.data['student_id'],
                "name":request.data['name'], 
                "competetion":request.data['competetion'],
                "solve1":solve1,
                "solve2":solve2,
                "solve3":solve3,
                "solve4":solve4,
                "solve5":solve5,
                "solve_best":min(float(participant.solve_best), float(solve_best)),
                "solve_avg":min(float(participant.solve_avg), float(solve_avg))
            }
        else:
            result_data = {
                "student_id": request.data['student_id'],
                "name":request.data['name'], 
                "competetion":participant.competetion,
                "solve1":participant.solve1,
                "solve2":participant.solve2,
                "solve3":participant.solve3,
                "solve4":participant.solve4,
                "solve5":participant.solve5,
                "solve_best":min(float(participant.solve_best), float(solve_best)),
                "solve_avg":min(float(participant.solve_avg), float(solve_avg))
            }
        serializer = ParticipantSerializer(participant, data=result_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        participant = get_object_or_404(Participant, pk=pk)
        participant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)