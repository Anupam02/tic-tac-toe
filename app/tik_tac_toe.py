import numpy as np
import re

from typing import Optional


class TicTakToe:

    __symbols = ['X', 'O', '*', '@']

    def __init__(self, nrow: Optional[int] = 3, ncol: Optional[int] = 3) -> None:
        self._nrow = nrow
        self._ncol = ncol
        self._input_search_pattern = r"^\d+\s*,\s*\d$"

    def generate_board(self, symbol: Optional[str] = " ") -> None:
        self._default_symbol = symbol
        self._board = np.array([[symbol]*self._ncol]*self._nrow)

    def display_board(self) -> None:
        print('The Current Status of Board ->->')
        for r in range(self._nrow):
            print(' | '.join(self._board[r, :]))
            if r == self._nrow - 1:
                continue
            print('***'* len(self._board[r, :]))
        print('\n')

    def display_board_coordinate_reference(self) -> None:
        for r in range(self._nrow):
            for c in range(self._ncol):
                _box_value = self._board[r][c]
                if c == self._ncol - 1:
                    if _box_value == self._default_symbol:
                        print(f"({r}, {c})")
                    else:
                        print(f" {_box_value}  ")
                else:
                    if _box_value == self._default_symbol:
                        print(f"({r}, {c})", end=" | ")
                    else:
                        print(f"   {_box_value}  ", end=" | ")
            if r == self._nrow - 1:
                continue
            print('******' * (self._ncol+1))
        print('\n')

    def accept_players(self, nplayer: Optional[int] = 2) -> None:
        self._nplayer = nplayer
        self._players_symbol_map = dict()
        for _player_no in range(nplayer):
            _player_name = input(f"Player Name {_player_no+1}: ")
            while True:
                _player_symbol = input(f"Please select a symbol: {' | '.join(TicTakToe.__symbols)} : ")
                if _player_symbol in TicTakToe.__symbols:
                    if _player_symbol not in self._players_symbol_map.values():
                        break
                    else:
                        print(f"Invalid Symbol: {_player_symbol}, this symbol has already been taken by another player.")
                else:
                    print(f"Invalid Symbol: {_player_symbol}, Please select a Valid Symbol.")

            self._players_symbol_map[_player_name] = _player_symbol

    def reset_board(self, symbol: Optional[str] = " ") -> None:
        for r in range(self._nrow):
            for c in range(self._ncol):
                self._board[r][c] = symbol
    
    def is_player_winner(self, player: str, symbol: str) -> bool:
        if all(item == symbol for item in self._board[0, :]) or \
            all(item == symbol for item in self._board[:, 0]) or \
            all(item == symbol for item in self._board[1, :]) or \
            all(item == symbol for item in self._board[:, 1]) or \
            all(item == symbol for item in self._board[2, :]) or \
            all(item == symbol for item in self._board[:, 2]) or \
            all(item == symbol for item in self._board.diagonal()) or \
            all(item == symbol for item in self._board[::-1].diagonal()):
            return True
        return False

    def check_winner(self) -> bool:
        is_winner_found = False
        print(f"The current Board:")
        self.display_board()
        for _player, _symbol in self._players_symbol_map.items():
            if self.is_player_winner(_player, _symbol):
                is_winner_found = True
                print(f"Congrations !!! {_player} Won !!!")
                break
        if is_winner_found:
            return True
        return False

    def start(self):
        players = list(self._players_symbol_map.keys())
        count = 0
        player_in_queue = players[count]
        player_in_queue_symbol = self._players_symbol_map[player_in_queue]
        while True:
            print(f"Hey {player_in_queue} Have a Look at the coordinates for the game:")
            self.display_board_coordinate_reference()
            while True:
                input_str = input(f"Please enter the comma(,) separated coordinates for input[{player_in_queue_symbol}]: ")
                if re.search(self._input_search_pattern, input_str):
                    r, c = map(int, input_str.split(","))
                    break
                else:
                    print("Invalid Input format for coordinates, Please enter with format: x-cor, y-cor")

            if self._board[r][c] == self._default_symbol:
                self._board[r][c] = player_in_queue_symbol
                self.display_board()
                if self.is_player_winner(player_in_queue, player_in_queue_symbol):
                    print(f"Congratulations !!! {player_in_queue} :) You Won.")
                    break
                count += 1
                player_in_queue = players[count % self._nplayer]
                player_in_queue_symbol = self._players_symbol_map[player_in_queue]
             
            else:
                print(f'Invalid Move {player_in_queue}!!! {r}, {c} is already filled, try some other coordinates!!')
                self.display_board()
            
            if count >= self._nrow * self._ncol:
                print(f"Hey {players[0]} and {players[1]}, you both played well, Its a Tie.")
                break


