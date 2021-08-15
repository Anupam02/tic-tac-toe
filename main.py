from app.tik_tac_toe import TicTakToe


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
