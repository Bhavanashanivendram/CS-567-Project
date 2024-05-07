import unittest
from sports_team_manager import *

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("John Doe", 30, "Forward", {"goals": 5, "assists": 3})

    def test_update_stats(self):
        # Test case to update player's statistics
        self.player.update_stats({"goals": 2, "assists": 1})
        self.assertEqual(self.player.stats, {"goals": 7, "assists": 4})

    def test_get_stat(self):
        # Test case to get a specific statistic of the player
        self.assertEqual(self.player.get_stat("goals"), 5)
        self.assertEqual(self.player.get_stat("saves"), 0)  # Test non-existing stat

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team("Sharks")
        self.player = Player("Jane Doe", 27, "Goalie", {"saves": 15})

    def test_add_player(self):
        # Test case to add a player to the team
        self.team.add_player(self.player)
        self.assertIn(self.player, self.team.roster)

    def test_remove_player(self):
        # Test case to remove a player from the team
        self.team.add_player(self.player)
        self.team.remove_player("Jane Doe")
        self.assertNotIn(self.player, self.team.roster)

    def test_find_player(self):
        # Test case to find a player in the team's roster
        self.team.add_player(self.player)
        found = self.team.find_player("Jane Doe")
        self.assertEqual(found, self.player)
        self.assertIsNone(self.team.find_player("Nobody"))  # Test non-existing player

    def test_add_game(self):
        # Test case to add a game record to the team
        self.team.add_game("Tigers", 3, 2)
        self.assertEqual(len(self.team.games), 1)
        self.assertEqual(self.team.games[0]['team_score'], 3)

    def test_get_win_loss_record(self):
        # Test case to get the win-loss record of the team
        self.team.add_game("Tigers", 2)
        self.team.add_game("Eagles", 1, 2)
        wins, losses = self.team.get_win_loss_record()
        self.assertEqual(wins, 1)
        self.assertEqual(losses, 1)

    def test_calculate_team_stat_average(self):
        # Test case to calculate the average statistic value for the team
        self.team.add_player(self.player)
        self.team.add_player(Player("Bob Smith", 22, "Striker", {"goals": 10}))
        avg_saves = self.team.calculate_team_stat_average("saves")
        avg_goals = self.team.calculate_team_stat_average("goals")
        self.assertEqual(avg_saves, 7.5)
        self.assertEqual(avg_goals, 5)

class TestSportsTeamManager(unittest.TestCase):
    def setUp(self):
        self.manager = SportsTeamManager()

    def test_create_team(self):
        # Test case to create a new team
        self.manager.create_team("Sharks")
        self.assertIn("Sharks", self.manager.teams)
        self.manager.create_team("Sharks")
        self.assertEqual(len(self.manager.teams), 1)  # Ensure no duplicate teams

    def test_delete_team(self):
        # Test case to delete a team
        self.manager.create_team("Sharks")
        self.manager.delete_team("Sharks")
        self.assertNotIn("Sharks", self.manager.teams)
        self.manager.delete_team("Sharks")  # Test deleting non-existent team

    def test_add_player_to_team(self):
        # Test case to add a player to a team
        self.manager.create_team("Sharks")
        player = Player("Alice Jones", 24, "Midfielder", {"goals": 3})
        self.manager.add_player_to_team("Sharks", player)
        self.assertIn(player, self.manager.teams["Sharks"].roster)

    def test_remove_player_from_team(self):
        # Test case to remove a player from a team
        self.manager.create_team("Sharks")
        self.manager.add_player_to_team("Sharks", Player("Alice Jones", 24, "Midfielder", {"goals": 3}))
        self.manager.remove_player_from_team("Sharks", "Alice Jones")
        self.assertEqual(len(self.manager.teams["Sharks"].roster), 0)

    def test_get_team_stats(self):
        # Test case to get the statistics of a team
        self.manager.create_team("Sharks")
        self.manager.teams["Sharks"].add_game("Tigers", 3, 2)
        self.manager.teams["Sharks"].add_game("Eagles", 1, 2)
        self.manager.get_team_stats("Sharks")

if __name__ == '__main__':
    unittest.main()
