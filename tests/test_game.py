from pytest import mark
import numpy as np

@mark.board
class GridSizeTests:
    def test_grid_size(self, tic_tac_toe_object):
        row, col = tic_tac_toe_object._board.shape
        assert row == 3
        assert col == 3

    def test_grid_with_default_symbol(self, tic_tac_toe_object):
        board = tic_tac_toe_object._board
        default_symbol = tic_tac_toe_object._default_symbol
        assert np.all(board == default_symbol)
