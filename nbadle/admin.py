from django.contrib import admin
from .models import Team, Player, User, UserTeam, Game


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference', 'team_code')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'position', 'ppg', 'apg', 'rpg', 'spg', 'bpg', 'mpg', 'tpg', 'offensive_rating', 'defensive_rating', 'height', 'weight', 'college')
    list_filter = ('team',)
    search_fields = ('name', 'team__name')


admin.site.register(User)
admin.site.register(UserTeam)
admin.site.register(Game)
