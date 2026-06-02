import unittest
from io import StringIO
from unittest.mock import patch

from dragon_and_avatars_game import Avatar, can_dragon_win, simulate_game, solve


class DragonAndAvatarsGameTests(unittest.TestCase):
    def test_dragon_wins_when_it_survives_every_duel(self):
        avatars = [Avatar(health=3, attack=2), Avatar(health=4, attack=1)]

        result = simulate_game(dragon_health=12, dragon_attack=3, avatars=avatars)

        self.assertTrue(result.dragon_won)
        self.assertEqual(result.avatars_defeated, 2)
        self.assertEqual(result.dragon_health_left, 11)

    def test_dragon_loses_when_an_avatar_outlasts_it(self):
        avatars = [Avatar(health=6, attack=5)]

        result = simulate_game(dragon_health=9, dragon_attack=2, avatars=avatars)

        self.assertFalse(result.dragon_won)
        self.assertEqual(result.avatars_defeated, 0)
        self.assertEqual(result.dragon_health_left, 0)

    def test_can_dragon_win_wrapper(self):
        self.assertTrue(can_dragon_win(10, 10, [Avatar(health=3, attack=2)]))

    def test_invalid_values_raise(self):
        with self.assertRaisesRegex(ValueError, "dragon_health must be greater than 0"):
            simulate_game(dragon_health=0, dragon_attack=1, avatars=[])
        with self.assertRaisesRegex(ValueError, "dragon_attack must be greater than 0"):
            simulate_game(dragon_health=1, dragon_attack=0, avatars=[])
        with self.assertRaisesRegex(ValueError, "avatar.health must be greater than 0"):
            simulate_game(dragon_health=1, dragon_attack=1, avatars=[Avatar(health=0, attack=1)])
        with self.assertRaisesRegex(ValueError, "avatar.attack must be greater than 0"):
            simulate_game(dragon_health=1, dragon_attack=1, avatars=[Avatar(health=1, attack=0)])

    def test_solve_raises_for_incomplete_avatar_data(self):
        with patch("sys.stdin", StringIO("10 2 1 5")):
            with self.assertRaisesRegex(ValueError, "Invalid input format. Expected:"):
                solve()

    def test_solve_raises_for_empty_input(self):
        with patch("sys.stdin", StringIO("")):
            with self.assertRaises(ValueError):
                solve()


if __name__ == "__main__":
    unittest.main()
