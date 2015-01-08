#!/usr/bin/env python

# Copyright (C) 2015 Devesh Saini(futuredevesh@gmail.com).
#
# This file is part of num2word.
#
#     num2word is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     num2word is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with num2word.  If not, see <http://www.gnu.org/licenses/>.

data_first_ones = ['', 'Bi', 'Tri', 'Quadri', 'Quinti', 'Sexti', 'Septi', 'Octi', 'Noni'] #Two first are empty, one for zero and one for one.

ones_suffix = "llion" #Suffix for one's numbers.

data_ones = {'0': '', '1':'un', '2':'duo', '3':'tre', '4':'quattuor', '5':'quin', '6':'sex', '7':'septen', '8':'octo', '9':'novem'}

data_tens = {"0":"", "1":'dec', "2":'vigin', "3":'trigin', "4":'quadragin', "5":'quinquagin', "6":'sexagin', "7":'septuagin', "8":'octogin', "9":'nonagin'}

tens_suffix = "illion" #Suffix for ten's numbers.

data_hundreds = {"0":"", "1":'cen', "2":'duocen', "3":'trecen', "4":'quadringen', "5":'quingen', "6":'sescen', "7":'septingen', "8":'octingen', "9":'nongen'}

hundreds_suffix = "tillion" #Suffix for hundred's names.

data_thousands = 'millia'

thounsands_suffix = "tillion" #Suffix for thousand's names.

def combine(arg_list, sep): #"arg_list" is a list and "sep" is a seperator string.

	"""Combines strings from a list with same order with 'seperator' between elements"""

	return sep.join(arg_list)

def words(pre_card, main=True):

    wordslist = []

    for i in range(3, pre_card+1):

        wordslist.append(_words_(i))

    return wordslist

def _words_(pre_card, main=True): #pre_card stands for prefix cardial.

    "Gives words. 'type' are 'pt', 'pre_card' means for powers of ten and prefix cardinal numbers."

    str_precard = str(pre_card)

    if pre_card < 1:

        return ""

    elif pre_card < 10:

        if main: #If function is called with external expression.

            ones = data_first_ones[pre_card - 1]

            return ones + ones_suffix

        elif not main: #If function is called from itself i.e. recursively.

            return data_ones[str(pre_card)]

    elif 10 <= pre_card < 100:

        tens = data_tens[str_precard[0]]

        ones = data_ones[str_precard[1]]

        if main:
            suffix = tens_suffix

        elif not main:
            suffix = ""

        return combine([ones, tens, suffix], '-')

    elif 100 <= pre_card < 1000:

        hundreds = data_hundreds[str_precard[0]]

        remain_num = int(str_precard[1:])

        rest = _words_(remain_num, False) #Calling itself i.e. recursive, So, False

        if int(remain_num) >= 10:
            suffix = tens_suffix

        else:
            suffix = hundreds_suffix

        return combine([hundreds, rest, suffix], '-')

    else: pass

if __name__ == "__main__":

    print words(input("Enter Prefix Cardinal Number : "))
