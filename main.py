###### The Higher_Lower_Game ######
# from random import randint
# from art import logo
# from art import vs
# from game_data import data

# number_dice = len(data)
#  #user choice#
# game = True
# while game :  
#     A_dice = randint(0, number_dice - 1)
#     B_dice = A_dice
#     while B_dice == A_dice:
#         B_dice = randint(0, number_dice - 1)
#         print(f"Compare A : {data[A_dice]['name']}, a {data[A_dice]['description']}, from {data[A_dice]['country']}.")
#         A = data[A_dice]['flower_count']
#         print(A)

#         print(f"Against B : {data[B_dice]['name']}, a {data[B_dice]['description']}, from {data[B_dice]['country']}.")
#         B = data[B_dice]['flower_count']
#         print(B)

#     #compare#
#     game = True
#     score = 0
#     while game and number_dice > 1   :
#         user_choice = input("Who has more flowers ? Type 'A' or 'B' : ").upper()
#         if user_choice == 'A' and A > B :
#             score+=1
#             print(f"You're right! , current score{score}")
#             data.remove(data[B_dice])
#             number_dice -= 1
#         elif user_choice == 'A' and A < B :
#             print(f"Sorry, that's wrong. Final score - {score}")
#             data.remove(data[B_dice])
#             number_dice -= 1
#             break
#         elif user_choice == 'B' and B > A :
#             score+=1
#             print(f"You're right! , current score = {score}")
#             data.remove(data[A_dice])
#             number_dice -= 1
#         else: 
#             print(f"Sorry, that's wrong. Final score = {score}")
#             data.remove(data[B_dice])
#             number_dice -= 1
#             break
   
# solution

import random

from art import logo, vs
from game_data import data


def game_loop():
    score = 0
    should_continue = True

    account_a = random.choice(data)

    while should_continue:
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {account_a['name']}, a {account_a['description']} from {account_a['country']}")
        print(vs)
        print(f"Compare B: {account_b['name']}, a {account_b['description']} from {account_b['country']}")

        decision = input("Who has more followers ? Type 'A' or 'B' ").lower()

        if account_a['follower_count'] > account_b['follower_count']:
            answer = "a"
        elif account_b['follower_count'] > account_a['follower_count']:
            answer = "b"
            account_a = account_b
        else:
            answer = "equal"

        if decision == answer:
            score += 1
            print(f"You are correct. Your current score is {score}")
        elif answer == "equal":
            score += 1
            print(f"They are equal. Your current score is {score}")
        else:
            print(f"That was incorrect. Your final score is {score}")
            should_continue = False


print(logo)
game_loop()