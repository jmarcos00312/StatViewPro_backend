from django.contrib import admin
from .models import Team, Player, User, UserTeam, Game


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference', 'team_code')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'college', 'team')
    list_filter = ('team',)
    search_fields = ('name', 'team__name')


admin.site.register(User)
admin.site.register(UserTeam)
admin.site.register(Game)
