This is a simple tic tac toe implementation in Python with Command Line interface, It takes a 3 x 3 matrix with 2 players.

- What is the aim of this project for?
This is to implement a tic tac toe with 3 approaches , manual/bot/minimax algorithm


- What is the default game configuration?<br>
This starts with 2 players , firstly by asking their names and choosing their symbols they want to go with.

- What is the input format?<br>
There are multple ways to take input from players, but in my current project I am taking input as x coordinates, y coordinates

(0, 0) | (0, 1) | (0, 2)

+++++++++++++++

(1, 0) | (1, 1) | (1, 2)

+++++++++++++++

(2, 0) | (2, 1) | (2, 2)

## installation 
#### create an image with name tic-tac-toe, it would build the image with all dependency present in requirements.txt
` docker build tic-tac-toe:v1.0`
#### run it with
` docker run -it tic-tac-toe:v1.0 python main.py --game-mode manual/bot`
### to run automated mode with computer( minimax algorithm)
### tkinter should be installed [ sudo apt install python3-tk]
` python main.py --game-mode min-max`
## How to Contribute

### Submitting an issue

Use the [issue tracker](https://github.com/mjbrusso/game2dboard/issues) to submit bug reports and features or enhancements requests.


### Translating

You can contribute by translating this document into other languages ​​(except *en* and *pt_br*).

### Submitting a pull request

If you can improve anything in this project, feel free to add a [pull request](https://github.com/Anupam02/tic-tac-toe/pulls).


## License

tic-tac-toe is under [MIT license](https://github.com/mjbrusso/game2dboard/blob/master/LICENSE). It can be reused within proprietary software provided that all copies of the licensed software include a copy of the MIT License terms and the copyright notice.
