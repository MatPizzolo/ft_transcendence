from django.http import JsonResponse

from ..models import CustomUser
from api.tournament.models import Match
from api.tournament.models import Tournament
from django.db.models import Q


def get_kpi(request, user_id):
    if request.method != 'GET':
        return JsonResponse({
            "status": "Method not allowed"
        }, status=405)
    try:
        user = CustomUser.objects.get(pk=user_id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"status": "User not found"}, status=404)

    matches = Match.objects.filter(Q(player1=user) | Q(player2=user))
    wins = matches.filter(winner=user)
    winrate = round(len(wins) / len(matches), 2) if len(matches) != 0 else 0
    tournament_wins = Tournament.objects.filter(winner=user)

    res = {
        "games_played": len(matches),
        "wins": len(wins),
        "winrate": winrate * 100,
        "tournaments_won": len(tournament_wins),
    }

    return JsonResponse(res)