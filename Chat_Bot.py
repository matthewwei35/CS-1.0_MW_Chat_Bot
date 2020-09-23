# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

# Combine functions and conditionals to get a response from the bot
def get_food_bot_response(user_response):
    # Bot reponses for cuisines
    bot_response_chinese = ['Hotpot!', 'Dumplings!', 'Peking Roasted Duck!', 'Chow Mein!', 'Steamed Vermicelli Rolls!']
    bot_response_italian = ['Lasagna', 'Risotto!', 'Truffles!', 'Gelato!', 'Pizza!']
    bot_response_mexican = ['Horchate!', 'Chicken Tamales!', 'Chilaquiles!', 'Tostadas!', 'Enchiladas!']
    bot_response_japanese = ['Sushi!', 'Tempura!', 'Tofu!', 'Ramen!', 'Udon!']

    # choice() randomly returns a response from a list
    if user_response == "Chinese":
        return choice(bot_response_chinese)
    elif user_response == "Italian":
        return choice(bot_response_italian)
    elif user_response == "Mexican":
        return choice(bot_response_mexican)
    elif user_response == "Japanese":
        return choice(bot_response_japanese)
    elif user_response == "done":
        return "See you next meal!"
    else:
        return "Sorry, I don't know that cuisine."

# Title and instructions of chat bot
print("~~~~ Welcome to Food Bot ~~~~")
print("- We reccommend dishes in a specfic cuisine you enter in, an example of a cuisine would be 'Chinese'.")
print("- If you're finished, type in 'done'.")

# Stores an empty string so we assign a value later
user_response = ""

# Keeps repeating and asking 'What cuisine are you craving right now?:' while user_response is not equal to 'done'
# When user_response is equal to 'done', the loop ends
while user_response != "done":
    user_response = input("What cuisine are you craving right now?: ")
    bot_response = get_food_bot_response(user_response)
    print(bot_response)