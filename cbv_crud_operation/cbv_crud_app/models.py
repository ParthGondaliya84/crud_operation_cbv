from django.db import models

class TeamDetail(models.Model):
    team_name = models.CharField(max_length=70)
    leader_name = models.CharField(max_length=70)
    email = models.EmailField(null=False)
    number = models.IntegerField()
    total_employee = models.IntegerField()

    def __str__(self):
        return self.team_name
    