# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/27 23:23:09 by adbaich           #+#    #+#              #
#    Updated: 2022/03/06 18:50:16 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
leng = len(sys.argv)
if leng != 1:
	while leng > 1:
		leng += -1
		txt = sys.argv[leng]
		res = txt.swapcase()
		if leng != 1:
			print(res[::-1], end = ' ')
		else:
			print(res[::-1])
else:
	sys.exit()