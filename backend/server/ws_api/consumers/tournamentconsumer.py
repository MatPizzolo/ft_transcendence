import json
from channels.generic.websocket import WebsocketConsumer
from ws_api.python_pong.Player import Player
from ws_api.python_pong.Game import Game
from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Q
import math
from api.tournament.models import Tournament
import random
from icecream import ic

class TournamentConsumer(WebsocketConsumer):
    list_of_player_channels = {}
    list_of_player_objects = {}
    list_of_matches = {}
    list_of_rounds = {}
    tournament_object = None
    tournament_admin_id = None
    tournament_ended = False
    tournament_rounds_to_complete = 0

    # Define constants for commands
    START_TOURNAMENT = 'start_tournament'
    START_MATCH = 'start_match'
    END_MATCH = 'end_match'
    START_ROUND = 'start_round'
    END_ROUND = 'end_round'
    ADD_PLAYER = 'add_player'
    REMOVE_PLAYER = 'remove_player'
    LIST_PLAYERS = 'list_players'
    LIST_MATCHES = 'list_matches'
    LIST_ROUNDS = 'list_rounds'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = None
        self.player_object = None

# Get User/Tourn
    def get_user(self, pk):
        from api.userauth.models import CustomUser as User
        try:
            user = get_object_or_404(User, pk=pk)
            if user is None:
                return None
            self.player_object = user
            self.list_of_player_objects[self.client_id] = self.player_object
            self.list_of_player_channels[self.client_id] = self.channel_name
            ic(f'Found user {user.username} with channel_name {self.channel_name}')
            return user
        except Exception as e:
            print(e)
            return None

    def get_tournament(self, pk):
        try:
            tournament = get_object_or_404(Tournament, pk=pk)
            if tournament is None:
                return None
            self.tournament_object = tournament
            ic(f'Found tournament {tournament.name}')
            return tournament
        except Exception as e:
            print(e)
            return None
# ---------------------------------------------


# Connect and Disconnect => Receive
    def connect(self):
        query_string = self.scope['query_string'].decode('utf-8')
        query_params = parse_qs(query_string)
        self.tournament_id = self.scope['url_route']['kwargs']['tournament_id']
        self.client_id = query_params['client_id'][0]

        # Get the user and see if they exist before accepting the connection
        self.player_object = self.get_user(self.client_id)
        if self.player_object is None:
            self.close()
            return
        

        self.accept()

        # Add client to the group channel
        print(f'Adding {self.client_id} to group {self.tournament_id}')
        self.channel_layer.group_add(
            str(self.tournament_id),
            self.channel_name
        )
        self.channel_layer.group_add(
            str(self.client_id),
            self.channel_name
)

        if self.tournament_admin_id is None:
            self.tournament_admin_id = self.client_id
            # Respond to the client that they are the tournament admin
            self.send_info_to_client('tournament_admin', {})

        self.broadcast_to_group(
            self.tournament_id,
            'new_player',
            {
                'tournament_id': self.tournament_id,
                'players': self.list_of_player_channels,
                'tournament_admin_id': self.tournament_admin_id
            }
        )
        
    def disconnect(self, close_code):
        # Remove client from the group channel
        self.channel_layer.group_discard(
            str(self.tournament_id),
            self.channel_name
        )
        # Remove client from the list of players or observers
        if self.client_id in self.list_of_player_channels:
            del self.list_of_player_channels[self.client_id]

        # Send info of group status every time a client leaves
        self.broadcast_to_group(
            str(self.tournament_id),
            'tournament_info',
            {
                'tournament_id': self.tournament_id,
                'players': self.list_of_player_channels,
                'matches': self.list_of_matches,
                'rounds': self.list_of_rounds,
                'tournament_admin_id': self.tournament_admin_id
            }
        )

    def receive(self, text_data):
        try:
            data = json.loads(text_data)
            command = data.get('command')

            if command == self.START_TOURNAMENT:
                self.start_tournament()
            elif command == self.START_ROUND:
                self.start_round()
            elif command == self.LIST_PLAYERS:
                self.send_info_to_client(self.LIST_PLAYERS, self.list_of_player_channels)
            elif command == self.LIST_MATCHES:
                self.send_info_to_client(self.LIST_MATCHES, self.list_of_matches)
            elif command == self.LIST_ROUNDS:
                self.send_info_to_client(elf.LIST_ROUNDS, self.list_of_rounds)
            else:
                print(f"Unknown command: {command}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
        except Exception as e:
            print(f"Error in receive method: {e}")
# ---------------------------------------------

# Messaging Function
    def broadcast(self, event):
        command = event['command']
        data = event['data']
        print(f'Sending message to client {self.client_id} with data: {data}')
        self.send(text_data=json.dumps({
            'type': command,
            'data': data
        }))


    def broadcast_to_group(self, group_name, command, data):
        print(f'Channel Broadcasting {command} to group {group_name}')
        self.channel_layer.group_send(
            group_name,
            {
                'type': 'broadcast',
                'command': command,
                'data': data
            }
        )

    def send_info_to_client(self, command, data):
        print(f'Sending message to client {self.client_id} with data: {data}')
        self.send(text_data=json.dumps({
            'type': command,
            'data': data
        }))
# --------------------------------------------

    def start_tournament(self):
        self.tournament_admin_id = self.client_id
        self.get_tournament(self.tournament_id)
        self.send_info_to_client('tournament_initialized', {})
        self.broadcast_to_group(
            str(self.tournament_id),
            'tournament_info',
            {
                'tournament_id': self.tournament_id,
                'players': self.list_of_player_channels,
                'matches': self.list_of_matches,
                'rounds': self.list_of_rounds,
                'tournament_admin_id': self.tournament_admin_id
            }
        )


# Start and end rounds and matches
    def start_round(self):
        # Add your tournament matchmaking logic here


        self.matchmaking_logic()

        # Send info of group status every time a new client joins
        self.broadcast_to_group(
            str(self.tournament_id),
            'tournament_info',
            {
                'tournament_id': self.tournament_id,
                'players': self.list_of_player_channels,
                'matches': self.list_of_matches,
                'rounds': self.list_of_rounds,
                'tournament_admin_id': self.tournament_admin_id
            }
        )

    def matchmaking_logic(self):
        try:
            tournament = self.tournament_object
            players = tournament.players.all()

            if players.count() % 2 != 0:
                sit_out_player = random.choice(players)
            else:
                sit_out_player = None

            # Example:
            self.tournament_rounds_to_complete = self.calculate_rounds(players.count())
            if tournament.round >= self.tournament_rounds_to_complete:
                winner = max(players, key=lambda player: self.calculate_player_score(player, tournament=tournament))
                tournament.winner = winner
                tournament.end_date = timezone.now()
                tournament.save()
                self.broadcast_to_group(
                    str(self.tournament_id),
                    'tournament_info',
                    {
                        'tournament_id': self.tournament_id,
                        'players': self.list_of_player_channels,
                        'matches': self.list_of_matches,
                        'rounds': self.list_of_rounds,
                        'tournament_admin_id': self.tournament_admin_id,
                        'winner': winner,
                    }
                )
                return

            if tournament.round == 0:
                sorted_players = sorted(players, key=lambda player: player.ELO, reverse=True)
            else:
                sorted_players = sorted(players, key=lambda player: self.calculate_player_score(player, tournament=tournament), reverse=True)
            matches = self.create_matches(sorted_players)
            self.list_of_matches = {match.id: match for match in matches}
            self.create_round(tournament, matches)

            tournament.save()

            # Prepare the response with match details
            match_data = []
            for match in matches:
                # Use a helper function to determine player role
                role = self.get_player_role(match)
                if role:
                    match_info = {
                        'match_id': match.id,
                        'current_round': tournament.round,
                        'total_rounds': self.tournament_rounds_to_complete,
                        'player1_id': match.player1.id,
                        'player2_id': match.player2.id,
                        'your_role': role,
                    }
                    match_data.append(match_info)

            # Broadcast the modified match_data
            self.broadcast_to_group(
                str(self.tournament_id),
                'matchmaking_info',
                {
                    'sit_out_player': sit_out_player, 
                    'matches': match_data,
                }
            )

        except Exception as e:
            # Handle specific exceptions as needed
            print(str(e))
# ---------------------------------------------

# Methods for creating round and matches
    def create_matches(sorted_players):
        from api.tournament.models import Match
        matches = []
        num_players = len(sorted_players)

        # Adjust the range to handle odd number of players
        for i in range(0, num_players - 1, 2):
            player1 = sorted_players[i]
            player2 = sorted_players[i + 1]

            player1_score = 0
            player2_score = 0
            winner = None

            match = Match(
                player1=player1,
                player2=player2,
                player1_score=player1_score,
                player2_score=player2_score,
                winner=winner,
                date_played=timezone.now(),
                active=True
            )
            
            match.save()
            matches.append(match)

        return matches

    def create_round(tournament, matches):
        from api.tournament.models import Round
        new_round = Round(tournament=tournament, round_number=tournament.round + 1)
        new_round.save()
        new_round.matches.set(matches)


    def get_player_role(self, match):
        if self.client_id == match.player1.id:
            return 'leftPlayer'
        elif self.client_id == match.player2.id:
            return 'rightPlayer'
        return None

    def calculate_rounds(num_players):
        return math.ceil(math.log2(num_players))

    def calculate_player_score(player, tournament=None):
        if not tournament:
            return 0

        latest_round = tournament.rounds.last()  # Get the latest round

        if latest_round:
            matches = latest_round.matches.filter(Q(player1=player) | Q(player2=player))
            player_score = sum(1 for match in matches if match.winner == player)
        else:
            player_score = 0

        return player_score
# ---------------------------------------------
