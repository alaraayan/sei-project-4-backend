from django.db import models

# Create your models here.

class Sprint(models.Model):
    sprint_name = models.CharField(max_length=50)
    # start_date = models.DateField()
    # end_date = models.DateField()

    def __str__(self):
        return f"{self.sprint_name}"


# class SprintGoal(models.Model):
#     goal_name = models.CharField(max_length=50)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     goal_description = models.CharField(max_length=250)

#     def __str__(self):
#         return f"{self.goal_name}"


# class Mood(models.Model):
#     mood_name = models.CharField(max_length=50)
#     mood_image = models.CharField(max_length=250)
#     sprint = models.ForeignKey(
#         Sprint,
#         related_name='moods',
#         on_delete=models.CASCADE
#     )

#     def __str__(self):
#         return f"{self.mood_name}"
