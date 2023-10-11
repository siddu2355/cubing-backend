from rest_framework import serializers
from .models import Participant

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = [
            "student_id",
            "name",
            "competetion",
            "solve1",
            "solve2",
            "solve3",
            "solve4",
            "solve5",
            "solve_best",
            "solve_avg",
        ]
    

