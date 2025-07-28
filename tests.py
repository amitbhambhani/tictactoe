import unittest

import pytest

import tictactoe as ttt


@pytest.mark.usefixtures("db_class")
class testGame(unittest.TestCase):
    def testChoice(self):
        layout = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
        }

        ttt.choice("-4", layout, "X")
        ttt.choice("12", layout, "O")
        for key in layout:
            self.assertEqual(layout[key], str(key))

        ttt.choice("1", layout, "X")
        self.assertEqual(layout[1], "X", "Choice 1 for X updates layout")

        ttt.choice("3", layout, "O")
        self.assertEqual(layout[3], "O", "Choice 3 for O updates layout")

    def testCheckWin(self):
        layout = {
            1: "X",
            2: "X",
            3: "X",
            4: "4",
            5: "5",
            6: "6",
            7: "O",
            8: "O",
            9: "O",
        }

        patterns = {"123", "456", "789", "159", "258", "357", "147", "369"}

        self.assertTrue(ttt.checkWin(layout, patterns))

        layout = {
            1: "X",
            2: "2",
            3: "X",
            4: "4",
            5: "5",
            6: "6",
            7: "O",
            8: "O",
            9: "9",
        }

        self.assertFalse(ttt.checkWin(layout, patterns))


if __name__ == "__main__":
    unittest.main()
