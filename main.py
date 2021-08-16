from app.tik_tac_toe import TicTakToe
from app.min_max_tik_tac_toe import GUI
import click


@click.command()
@click.option('--game-mode',
              '-gm',
              type=click.Choice(['manual', 'bot', 'min-max'], case_sensitive=False),
              help='game mode to run [ manual / bot]',
              required=True)
def main(game_mode):
    try:
        if game_mode == 'manual':
            manual_play()
        elif game_mode == 'bot':
            automatic_play()
        elif game_mode == 'min-max':
            min_max_play()
        else:
            print('Invalid Option')

    except Exception as e:
        print(e)


def manual_play():
    tc = TicTakToe()
    choice = True
    while choice:
        tc.start()
        while True:
            will_continue = input("Do you want to continue..(yes/no | y/n: ")
            will_continue_lower = will_continue.lower()
            if will_continue_lower in ["yes", "y"]:
                print("Starting a new game....")
                break
            elif will_continue_lower in ["no", "n"]:
                choice = False
                print("Thanks for playing...")
                break
            else:
                print("Please select any one of [ yes / no | y / n] ..")


def automatic_play():
    tc = TicTakToe()
    tc.automated_start()


def min_max_play():
    GUI().mainloop()


if __name__ == '__main__':
    main()
