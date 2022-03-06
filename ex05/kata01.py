# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adbaich <adbaich@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/01 18:46:04 by adbaich           #+#    #+#              #
#    Updated: 2022/03/01 18:55:00 by adbaich          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
    'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
for str1 in kata:
    print("{} was created by {}".format(str1, kata[str1]))
