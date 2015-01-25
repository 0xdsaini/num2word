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

from sys import argv

data_first_ones = ['', 'Bi', 'Tri', 'Quadri', 'Quinti', 'Sexti', 'Septi', 'Octi', 'Noni'] #Two first are empty, one for zero and one for one.

ones_suffix = "llion" #Suffix for one's numbers.

data_ones = {'0': '', '1':'Un', '2':'Duo', '3':'Tre', '4':'Quattuor', '5':'Quin', '6':'Sex', '7':'Septen', '8':'Octo', '9':'Novem'}

data_tens = {"0":"", "1":'Dec', "2":'Vigin', "3":'Trigin', "4":'Quadragin', "5":'Quinquagin', "6":'Sexagin', "7":'Septuagin', "8":'Octogin', "9":'Nonagin'}

tens_suffix = "illion" #Suffix for ten's numbers.

data_hundreds = {"0":"", "1":'Cen', "2":'Duocen', "3":'Trecen', "4":'Quadringen', "5":'Quingen', "6":'Sescen', "7":'Septingen', "8":'Octingen', "9":'Nongen'}

hundreds_suffix = "tillion" #Suffix for hundred's names.

data_thousands = 'Millia'

thousands_suffix = "tillion" #Suffix for thousand's names.

def combine(arg_list, sep): #"arg_list" is a list and "sep" is a seperator string.

    """Combines strings from a list with same order with 'seperator' between elements"""

    no_empty = [] #no_empty is an filtered list of arg_list with having no empty strings.

    for i in arg_list:
        if not i == "":
            no_empty.append(i)

    return sep.join(no_empty)

def words(pre_card, main=True):

    """Words equivalent to range function. for example, if pre_card=5 is given
    then it will return a list of all words from latin powers 3 to 5 inclusively
    i.e. ['Billion', 'Trillion', 'Quadrillion']"""

    wordslist = []

    for i in range(2, pre_card+1):

        wordslist.append(_words_(i))

    return wordslist

def _words_(pre_card, main=True): #pre_card stands for prefix cardial.

    "Gives words. 'type' are 'pt', 'pre_card' means for powers of ten and prefix cardinal numbers respectively."

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

        tens_plus_suffix = combine([tens, suffix], '') #Between tens and suffix, there is NO SEPERATOR.

        return combine([ones, tens_plus_suffix], '-') #Between ones and tens_plus_suffix variable, there is dash(-) SEPERATOR.

    elif 100 <= pre_card < 1000:

        hundreds = data_hundreds[str_precard[0]] #Number of hundreds i.e. Cen, Duocen and so on...

        remain_num = int(str_precard[1:])

        rest = _words_(remain_num, False) #giving True will result in output with suffix, so False.

        hundreds_rest = combine([hundreds, rest], '-')

        if main:

            if 10 <= int(remain_num) < 20:
                suffix = tens_suffix

            else:
                suffix = hundreds_suffix

        else:
            suffix = ""

        return combine([hundreds_rest, suffix], '')

    elif 1000 <= pre_card < 1000000:

        thousands_num = int(str_precard[:-3]) #Recursively call itself to get the number of thousands in words.

        #BEGINS : For computing number of thousands and data_thousands management.
        if thousands_num > 1:
            thousands = combine([_words_(thousands_num, False), data_thousands], '-')

        else:
            thousands = data_thousands
        #ENDS : For computing number of thousands and data_thousands management.

        #BEGINS : For choosing the right suffix.
        if main:
            if 10 <= int(str_precard[-2:]) < 20: #In case of illion suffix if tens numbers are (10 <= x < 20), illion suffix would be used.
                suffix = tens_suffix

            else:
                suffix = thousands_suffix

        else:
            suffix = ""
        #ENDS : For choosing the right suffix.

        remain_num = int(str_precard[-3:])

        rest = _words_(remain_num, False) #Rest words, recursively computing using the remaining number

        rest_plus_suffix = combine([rest, suffix], '')

        return combine([thousands, rest_plus_suffix], '-')

if __name__ == "__main__":

    if argv[1:]:
        pre_card = int(argv[1])

    else:
        pre_card = input("Enter Prefix Cardinal Number : ")

    print words(pre_card)
