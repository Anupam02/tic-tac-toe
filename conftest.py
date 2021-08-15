from pytest import fixture
from app.tik_tac_toe import TicTakToe


@fixture()
def tic_tac_toe_object():
    tic_tac_toe_obj = TicTakToe()
    yield tic_tac_toe_obj
