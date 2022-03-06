# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 01:03:00 by adbaich           #+#    #+#              #
#    Updated: 2022/03/06 18:53:37 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
if len(sys.argv) == 2:
    try:
        num = int(sys.argv[1])
    except:
        sys.exit("AssertionError: argument is not an integer")
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    sys.exit("AssertionError: more than one argument are provided")