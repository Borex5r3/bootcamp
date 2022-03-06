# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/04 00:44:43 by adbaich           #+#    #+#              #
#    Updated: 2022/03/04 03:18:20 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import string
check = string.punctuation
if len(sys.argv) == 3:
    i = 0
    list1 = []
    list2 = []
    str1 = ""
    if sys.argv[1].isdigit():
        sys.exit("ERROR")
    for char in sys.argv[1]:
        if char not in check and char != ' ' and not char.isspace():
            str1 = str1 + char
        else:
            list1.append(str1)
            str1 = ""
            pass
    list1.append(str1)
    try:
        list2 =  [str for str in list1 if len(str) > int(sys.argv[2])]
    except:
        sys.exit("ERROR")
    print(list2)
else:
    sys.exit("ERROR")