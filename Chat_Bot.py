# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

def get_food_bot_response(user_response):
    bot_response_chinese = ['Hotpot!', 'Dumplings!', 'Peking Roasted Duck!', 'Chow Mein!', 'Steamed Vermicelli Rolls!']
    bot_response_italian = ['Lasagna', 'Risotto!', 'Truffles!', 'Gelato!', 'Pizza!']

    if user_response == "Chinese":
        return choice(bot_response_chinese)
    elif user_response == "Italian":
        return choice(bot_response_italian)
    elif user_response == "":
        pass
    elif user_response == "":
        pass
    elif user_response == "done":
        return "See you next meal!"
    else:
        return "Sorry, I don't know that cuisine."

print("~~~~ Welcome to Food Bot ~~~~")
print("We reccommend dishes in a specfic cuisine you enter in, an example would be 'Chinese'.")
print("If you are finished, type in 'done'.")

user_response = ""

while user_response != "done":
    user_response = input("What cuisine are you craving right now?: ")
    bot_response = get_food_bot_response(user_response)
    print(bot_response)