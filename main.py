import random

exit = False
user_points = 0
computer_points = 0


def is_win(user, computer):
    global user_points, computer_points
    if (user == 'r' and computer == 's') or \
            (user == 's' and computer == 'p') or \
            (user == 'p' and computer == 'r'):
        print("You win.")
        user_points += 1
    elif user == computer:
        print('It is a tie!')
    else:
        print("Computer win.")
        computer_points += 1


while not exit:
    options = ["rock", "paper", "scissors"]
    user = input("Choose 'r' for rock,'p' for paper,'s' for scissors, 'e' for exit: ")
    computer = random.choice(options)

    if user == 'e':
        print("Game Ended")
        exit = True
    elif user in ['r', 'p', 's']:
        computer_choice = random.choice(options)
        is_win(user, computer_choice)
    else:
        print("Invalid choice. Please choose again.")

print("Final Score:")
print(f"User Points: {user_points}")
print(f"Computer Points: {computer_points}")
