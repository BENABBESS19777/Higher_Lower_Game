###### The Higher_Lower_Game ######
from random import randint
from art import logo
from art import vs
from game_data import data

number_dice = len(data)
#user choice#
user_choice = randint(0,number_dice - 1 )
print(f"Compare A : {data[user_choice]['name']}, a {data[user_choice]['description']}, from {data[user_choice]['country']}.")
user_flowers = data[user_choice]['flower_count']
print(user_flowers)
data.remove(data[user_choice])

#computer choice#
computer_choice = randint(0, number_dice - 2)
print(f"Against B : {data[computer_choice]['name']}, a {data[computer_choice]['description']}, from {data[computer_choice]['country']}.")
computer_flowers = data[computer_choice]['flower_count']
print(computer_flowers)
print(data)

