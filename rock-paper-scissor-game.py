import random #importing random

rock =''' ROCK
    ______
---'______)
    (_______)
    (________)
    (_______)
---.(______)
'''
paper =''' PAPER
    _____
---'______)
    ________)_
    __________)
    _________)
---.______)
'''
scissor ='''  SCISSOR
      ______
----'_______)___
        ________)
     ___________)
    (______)
---.__(___)

'''

images=[rock,paper,scissor]

user_choice=int(input("what is your choice  ? Type 0 for rock ,1 for paper ,2 for scissros : \n"))#users choice
print(images[user_choice])

computer_choice=random.randint(0,2)#computer choice
print("computer choose :")
print(images[computer_choice])

if user_choice > 3 or user_choice <=0:
    print("you type a invalid number, you loose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif user_choice == 2 and computer_choice == 0:
    print("you loose !")
elif computer_choice > user_choice:
    print(" you loose!")
elif computer_choice < user_choice:
    print(" you win!")
elif compuer_choice == user_choice:
    print("match draw")







