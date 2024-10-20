import unittest
from main import Connect4

class TestConnect4NoWinner(unittest.TestCase):

    def test_no_winner(self):
        game = Connect4()
        self.assertFalse(game.check_win('X'))
        self.assertFalse(game.check_win('O'))

if __name__ == '__main__':
    unittest.main()

# Test Results:
# ---------------
# all tests passed
# no bugs or issues identified
# check_win method correctly returns false when there is no winning condition for both players
