class Player:
    def __init__(self, name, age, position, stats):
        self.name = name
        self.age = age
        self.position = position
        self.stats = stats  # stats is a dictionary containing various performance metrics

    def update_stats(self, game_stats):
        for key, value in game_stats.items():
            if key in self.stats:
                self.stats[key] += value
            else:
                self.stats[key] = value

    def get_stat(self, stat_name):
        return self.stats.get(stat_name, 0)

    def __str__(self):
        return f"{self.name}, Age: {self.age}, Position: {self.position}"

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = []
        self.games = []

    def add_player(self, player):
        pass
        print(f"Added {player.name} to {self.team_name}")

    def remove_player(self, player_name):
        self.roster = [player for player in self.roster if player.name != player_name]
        print(f"Removed {player_name} from {self.team_name}")

    def find_player(self, player_name):
        for player in self.roster:
            if player.name == player_name:
                return player
        return None

    def add_game(self, opponent, team_score, opponent_score):
        self.games.append({'opponent': opponent, 'team_score': team_score, 'opponent_score': opponent_score})
        print(f"Game added: {self.team_name} ({team_score}) vs {opponent} ({opponent_score})")

    def get_win_loss_record(self):
        wins = 0
        losses = 0
        for game in self.games:
            if game['team_score'] > game['opponent_score']:
                wins += 1
            else:
                losses += 1
        return wins, losses

    def display_roster(self):
        for player in self.roster:
            print(player)

    def calculate_team_stat_average(self, stat_name):
        total = sum(player.get_stat(stat_name) for player in self.roster)
        if len(self.roster) > 0:
            return total / len(self.roster)
        return 0

    def __str__(self):
        return f"Team: {self.team_name}, Players: {len(self.roster)}"

class SportsTeamManager:
    def __init__(self):
        self.teams = {}

    def create_team(self, team_name):
        if team_name not in self.teams:
            self.teams[team_name] = Team(team_name)
            print(f"Team created: {team_name}")
        else:
            print("Team already exists.")

    def delete_team(self, team_name):
        if team_name in self.teams:
            del self.teams[team_name]
            print(f"Team deleted: {team_name}")
        else:
            print("Team does not exist.")

    def add_player_to_team(self, team_name, player):
        if team_name in self.teams:
            self.teams[team_name].add_player(player)
        else:
            print(f"Team {team_name} does not exist.")

    def remove_player_from_team(self, team_name, player_name):
        if team_name in self.teams:
            self.teams[team_name].remove_player(player_name)
        else:
            print(f"Team {team_name} does not exist.")

    def get_team_stats(self, team_name):
        if team_name in self.teams:
            team = self.teams[team_name]
            wins, losses = team.get_win_loss_record()
            print(f"Stats for {team_name}: Wins: {wins}, Losses: {losses}")
        else:
            print(f"Team {team_name} does not exist.")