# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/04 19:37:37 by adbaich           #+#    #+#              #
#    Updated: 2022/03/05 15:50:20 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import time
import  sys
listy = range(1000)
# ret = 0
# def ft_progress(listy):
#     i = 0
#     for i in listy:
#         yield i
# for elem in ft_progress(listy):
#     print("-->" + str(elem))
#     ret += (elem + 3) % 5
# time.sleep(0.01)
# print()
# print(ret)
toolbar_width = 1000

# setup toolbar
print("[%s]" % (" " * toolbar_width), end = '')
sys.stdout.flush()
print("\b" * (toolbar_width+1), end = '') # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    print("=", end = '')
    sys.stdout.flush()
sys.stdout.write("]\n")