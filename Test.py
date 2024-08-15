from random import randint

print("Nhập Đấm,Lá,Kéo: ")
player = str(input())
computer = randint(0,2)


if computer == 0:
    computer_choice = "Dam"
elif computer == 1:
    computer_choice = "La"
else:
    computer_choice = "Keo"

print("---")
print("You Choose: " + player)
print("Computer Chooses: " + computer_choice)
print("---")

if player == computer_choice:
    print("Draw")
else:
    if player == "Keo":
        if computer_choice== "Dam":
            print("Lose")
        else:
            print("Win")

    elif player == "Dam":
        if computer_choice == "Keo":
            print("Win")
        else:
            print("Lose")

    elif player == "La":
        if computer_choice == "Keo":
            print("Lose")
        else:
            print("Win")

    else:
        print("Nhập sai!")