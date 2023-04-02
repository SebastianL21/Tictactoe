from tictactoe import player, actions, result, winner, terminal
import pytest


class TestPlayer:
    def test_player(self):
        board = [[None, None, None], [None, None, None], [None, None, None]]
        assert player(board) == "X"

    def test_player_X(self):
        board = [[None, "O", None], ["X", None, None], [None, None, None]]
        assert player(board) == "X"

    def test_player_O(self):
        board = [[None, "O", None], ["X", None, None], [None, "X", None]]
        assert player(board) == "O"


class TestActions:
    def test_actions(self):
        board = [["X", "X", None], ["O", "O", "X"], ["X", "O", "X"]]
        assert actions(board) == [(0, 2)]

    def test_actions_more(self):
        board = [["X", "X", None], ["O", None, "X"], [None, "O", "X"]]
        assert actions(board) == [(0, 2), (1, 1), (2, 0)]

    def test_actions_empty_board(self):
        board = [[None, None, None], [None, None, None], [None, None, None]]
        assert actions(board) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]


class TestResult:
    def test_result(self):
        board = [["X", "O", None], ["O", "O", "X"], ["X", "O", "X"]]
        action = (0, 2)
        assert result(board, action) == [["X", "O", "X"], ["O", "O", "X"], ["X", "O", "X"]]

    def test_result_more(self):
        board = [[None, "O", None], ["X", None, None], [None, "X", None]]
        action = (1, 1)
        assert result(board, action) == [[None, "O", None], ["X", "O", None], [None, "X", None]]

    def test_result_notvalidaction(self):
        with pytest.raises(Exception):
            board = [[None, "O", None], ["X", None, None], [None, "X", None]]
            action = (0, 1)
            result(board, action)


class TestWinner:
    def test_winner(self):
        board = [[None, "O", "X"], ["X", "O", None], ["X", "O", None]]
        assert winner(board) == "O"

    def test_winner_more(self):
        board = [["O", None, "X"], ["O", "X", None], ["X", None, "O"]]
        assert winner(board) == "X"

    def test_winner_none(self):
        board = [[None, None, "X"], ["O", None, None], ["X", None, None]]
        assert winner(board) is None


class TestTerminal:
    def test_termina(self):
        board = [[None, "O", "X"], ["X", "O", None], ["X", "O", None]]
        assert terminal(board) is True

    def test_terminal_no_winner(self):
        board = [["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]
        assert terminal(board) is True

    def test_terminal_still_playing(self):
        board = [[None, "O", "X"], ["X", None, None], ["X", "O", None]]
        assert terminal(board) is False
