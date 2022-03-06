# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 01:30:23 by adbaich           #+#    #+#              #
#    Updated: 2022/03/03 03:40:36 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys
check = string.punctuation
def text_analyzer(text = None):
    """
    This Magic Function takes a single string argument and displays the sums of its upper-case characters, lower-case characters,
    punctuation characters and spaces.
    """
    uppchar = 0
    lowchar = 0
    punct = 0
    space = 0
    if text is None:
        print("What is the text to analyze?")
        text = input(">> ")
    try:
        for char in text:
            if char in check:
                pass
            elif char.isalpha() or char.isdigit() or char == ' ':
                pass
            else:
                print("AssertionError: argument is not a string")
                return
    except:
        print("AssertionError: argument is not a string")
        return
    print("The text contains {} character(s):".format(len(text)))
    for char in text:
        if (char.isupper()):
            uppchar += 1
        elif char.islower():
            lowchar += 1
        elif char in check:
            punct += 1
        elif char == ' ':
            space += 1
    print(f"- {uppchar} upper letter(s)")
    print("- {} lower letter(s)".format(lowchar))
    print("- {} punctuation mark(s)".format(punct))
    print("- {} space(s)".format(space))
if __name__=="__main__":
    if len(sys.argv) <= 2:
        if len(sys.argv) == 2:
            text_analyzer(sys.argv[1])
        else:
            text_analyzer()
    else:
        sys.exit("More Than One Argument is provided")