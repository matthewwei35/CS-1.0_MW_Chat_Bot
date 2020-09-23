# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

def get_food_bot_response(user_response): 
  bot_response_chinese = ['Hotpot!', 'Dumplings!', 'Peking Roasted Duck!', 'Chow Mein!']

  if user_response == "chinese":
    return choice(bot_response_chinese)
  else:
    return "Come back for more! "

print("Welcome to Food Bot")
print("This bot reccommends specfic dishes in a certain category of cuisine")

user_response = ""

while user_response != "done":
  user_response = input("What are you craving right now?: ")
  bot_response = get_food_bot_response(user_response)
  print(bot_response)