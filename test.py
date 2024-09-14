import unittest
from rules import (
    BirthRule,
    LonelyDeathRule,
    StayAliveRule,
    OverPopulateRule,
)

class TestBirthRule(unittest.TestCase):
    def test_birth_rule_with_dead_cell_and_three_live_neighbors(self):
        self.assertEqual(
            BirthRule.apply(0,3), 1, "Dead cell with 3 live neighbors should be born."
        )

    def test_birth_rule_with_dead_cell_and_two_live_neighbors(self):
        self.assertIsNone(
            BirthRule.apply(0, 2), "Dead cell with 2 live neighbors should remain dead."
        )
    
    def test_birth_rule_with_alive_cell(self):
        self.assertIsNone(
            BirthRule.apply(1, 3), "Alive cell should not be affected by BirthRule."
        )
    
    def test_birth_rule_with_dead_cell_and_four_live_neighbors(self):
        self.assertIsNone(
            BirthRule.apply(0, 4), "Dead cell with 4 live neighbors should remain dead."
        )

class TestLonelyDeathRule(unittest.TestCase):
    def test_lonely_death_rule_with_alive_cell_and_one_live_neighbor(self):
        self.assertEqual(
            LonelyDeathRule.apply(1, 1),
            0,
            "Alive cell with 1 live neighbor should die."
        )

    def test_lonely_death_rule_with_alive_cell_and_zero_live_neighbors(self):
        self.assertEqual(
            LonelyDeathRule.apply(1, 0),
            0,
            "Alive cell with 0 live neighbors should die."
        )

    def test_lonely_death_rule_with_alive_cell_and_two_live_neighbors(self):
        self.assertIsNone(
            LonelyDeathRule.apply(1, 2),
            "Alive cell with 2 live neighbors should not be affected by LonelyDeathRule."
        )

    def test_lonely_death_rule_with_dead_cell(self):
        self.assertIsNone(
            LonelyDeathRule.apply(0, 1),
            "Dead cell should not be affected by LonelyDeathRule."
        )

if __name__ == '__main__':
    unittest.main()