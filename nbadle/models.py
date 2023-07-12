from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    team_code = models.CharField(max_length=3)
    
    def __str__(self):
        return self.name
    
    
class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    img_url = models.URLField()
    ppg = models.FloatField()
    apg = models.FloatField()
    rpg = models.FloatField()
    spg = models.FloatField()
    bpg = models.FloatField()
    offensive_rating = models.FloatField()
    defensive_rating = models.FloatField()
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    favorite_team = models.OneToOneField(Team, on_delete=models.SET_NULL, null=True, related_name='favorite_user')
    roster = models.ManyToManyField(Player, related_name='user_roster')
    following_players = models.ManyToManyField(Player, related_name='followers')
    teams = models.ManyToManyField(Team, through='UserTeam', related_name='users')
    
    def __str__(self):
        return self.name

class UserTeam(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name='userteams')
    
    def __str__(self):
        return self.name


class Game(models.Model):
    users = models.ManyToManyField(User)
    played_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    # Define other fields as per your requirements
