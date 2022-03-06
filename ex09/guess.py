# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/04 18:57:47 by adbaich           #+#    #+#              #
#    Updated: 2022/03/04 19:36:50 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import random
print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!\n")
num = random.randint(1, 99)
count = 1
while 1:
        guess = input("What's your guess between 1 and 99?\n>> ")
        if guess == "exit": sys.exit("Goodbye!\n")
        elif not guess.isdigit(): print("That's not a number.\n")
        else:
            guess = int(guess)
            if guess >= 1 and guess <= 99:
                if guess == 42: sys.exit(f"The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your {count} try!")
                elif guess > num: print("Too high!\n")
                elif guess < num: print("Too low!\n")
                else: sys.exit(f"Congratulations, you've got it!\nYou won in {count} attempts!")
                count += 1
            else:
                print("Check The Range!")