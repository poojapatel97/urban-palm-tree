import unittest

from dragon_and_avatars_game import Avatar, can_dragon_win, simulate_game


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
        with self.assertRaises(ValueError):
            simulate_game(dragon_health=0, dragon_attack=1, avatars=[])


if __name__ == "__main__":
    unittest.main()
