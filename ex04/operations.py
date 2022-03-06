# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 23:46:57 by adbaich           #+#    #+#              #
#    Updated: 2022/03/01 17:48:45 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
if len(sys.argv) == 1:
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    sys.exit("python operations.py 10 3")
elif len(sys.argv) == 3:
    print("Sum: %d" % (int(sys.argv[1]) + int(sys.argv[2])))
    print("Difference: %d" % (int(sys.argv[1]) - int(sys.argv[2])))
    print("Product: %d" % (int(sys.argv[1]) * int(sys.argv[2])))
    if int(sys.argv[2]) == 0:
        print("Quotient: Error (division by zero)")
        print("Remainder: Error (modulo by zero)")
    else:    
        print("Quotient: %g" % (int(sys.argv[1]) / int(sys.argv[2])))
        print("Remainder: %g" % (int(sys.argv[1]) % int(sys.argv[2])))
else:
    sys.exit("More Than One Argument is provided")