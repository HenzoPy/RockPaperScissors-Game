import random


def start():
    easy_parameters = ['paper', 'rock', 'scissors']
    mid_parameters = ['paper', 'rock', 'scissors', 'paper', 'rock', 'scissors']
    parameters = ['scissors', 'rock', 'rock', 'scissors', 'paper', 'scissors', 'paper', 'paper', 'rock']

    # Rules
    def rules(a, b):
        if a == b:
            return 'tie'

        elif a == 'rock' and b == 'paper':
            return b

        elif a == 'paper' and b == 'rock':
            return a

        elif a == 'rock' and b == 'scissors':
            return a

        elif a == 'scissors' and b == 'rock':
            return b

        elif a == 'paper' and b == 'scissors':
            return b

        elif a == 'scissors' and b == 'paper':
            return a

    def play(a, b, c):
        def verify(entry):
            if entry in parameters:
                return entry
            else:
                print('Invalid Parameter')
                print(f"Round would be restarted if {b} also enters wrong play")
                play(a, b, c)

        p1_score = p2_score = 0
        for i in range(c):
            print(f"Round {i+1}")
            first = verify(input(f"{a} Play: ").lower())
            second = verify(input(f"{b} Play: ").lower())

            if rules(first, second) == "tie":
                print("It's a tie!!!\n")
                print(f"Score: {a}: {p1_score} {b}: {p2_score}")

            elif rules(first, second) == first:
                print(f"{a} wins!!!\n")
                p1_score += 1
                print(f"Score: {a}: {p1_score} {b}: {p2_score}")

            elif rules(first, second) == second:
                print(f"{b} wins!!!\n")
                p2_score += 1
                print(f"Score: {a}: {p1_score} {b}: {p2_score}")

            else:
                print("Round Undecided!!!\n")
                c += 1

    # Player vs Computer
    def ai():

        def difficulty_settings():
            print("Levels\n1. Hard\n2. Medium\n3. Easy")
            difficulty = input("Select Level: ").lower()
            match difficulty:
                case 'hard':
                    simulate_hard()
                case 'medium':
                    simulate_medium()
                case 'easy':
                    simulate_easy()
                case _:
                    print("Invalid Parameter!!!")
                    difficulty_settings()

        def verify(entry):
            if entry in parameters:
                return entry
            else:
                print('Invalid Parameter')
                ai()

        def simulate_hard():
            p1_score = p2_score = 0

            for i in range(rounds):
                print(f"Round {i + 1}")
                first = verify(input(f"{player} Play: ").lower())
                second = random.choice(parameters)
                print(f"Computer Play: {second}")

                if rules(first, second) == "tie":
                    print("It's a tie!!!\n")
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == first:
                    print(f"{player} wins!!!\n")
                    p1_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == second:
                    print(f"Computer wins!!!\n")
                    p2_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

        def simulate_medium():
            p1_score = p2_score = 0

            for i in range(rounds):
                print(f"Round {i + 1}")
                first = verify(input(f"{player} Play: ").lower())
                second = random.choice(mid_parameters)
                print(f"Computer Play: {second}")

                if rules(first, second) == "tie":
                    print("It's a tie!!!\n")
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == first:
                    print(f"{player} wins!!!\n")
                    p1_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == second:
                    print(f"Computer wins!!!\n")
                    p2_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

        def simulate_easy():
            p1_score = p2_score = 0

            for i in range(rounds):
                print(f"Round {i + 1}")
                first = verify(input(f"{player} Play: ").lower())
                second = random.choice(easy_parameters)
                print(f"Computer Play: {second}")

                if rules(first, second) == "tie":
                    print("It's a tie!!!\n")
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == first:
                    print(f"{player} wins!!!\n")
                    p1_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

                elif rules(first, second) == second:
                    print(f"Computer wins!!!\n")
                    p2_score += 1
                    print(f"Score: {player}: {p1_score} Computer: {p2_score}")

        try:
            rounds = int(input("Enter number of rounds: "))
        except ValueError:
            print("Invalid value")
            ai()
        player = input("Enter your name: ")
        difficulty_settings()

    # Player vs Player
    def multiplayer():
        player_1 = input("Player 1 enter your name: ")
        player_2 = input("Player 2 enter your name: ")
        try:
            rounds = int(input("Enter number of rounds: "))
        except ValueError:
            print("Invalid value")
            multiplayer()
        play(player_1, player_2, rounds)

    mode = input("Select Mode: ").lower()

    # Selection For Vs Human or AI
    match mode:
        case 'auto':
            ai()
        case 'multiplayer':
            multiplayer()
        case _:
            print("Invalid Mode")
            start()

