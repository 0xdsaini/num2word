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

"""A library to convert number into English words and perform basic
arithmatic operations i.e. addition, subtraction, multiplication and
division on the go.
"""

from words import words

class Verbal(object):

    def __init__(self, num):

        self.num = num
        self.str_num = str(num)

        self.numlist = [x for x in str(num)]

        self.data_ones = {"0":"", "1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
        self.data_tens = {"10":"Ten", "11":"Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen", "18":"Eighteen", "19":"Nineteen", "2":"Twenty", "3":"Thirty", "4":"Fourty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}

        self.data_hundreds = "Hundred"
        self.data_thousands = "Thousand"
        self.data_millions = "Million"

        self.list = [self.data_ones, self.data_tens, self.data_hundreds, self.data_thousands, self.data_millions]

        latin_range = map(lambda x: x/3, self.get_range(len(self.str_num)))
        latin_min = latin_range[0]

        self.list.extend( words(latin_min) )

    def __add__(self, num2):

        if type(num2) in [int, long]:

            return self._get_num_(self.num + num2)

    def __sub__(self, num2):

        if type(num2) in [int, long]:

            return self._get_num_(self.num - num2)

    def __mul__(self, num2):

        if type(num2) in [int, long]:

            return self._get_num_(self.num * num2)

    def __div__(self, num2):

        if type(num2) in [int, long]:

            return self._get_num_(self.num // num2)
        
    def __repr__(self):

        return "<num2word.Verbal>"

    def _get_list_(self, num):
        """Returns a list of one digit numbers from a string."""

        return [x for x in str(num)]

    def get_range(self, str_len):

        actual_len = str_len - 1 #number of maximum possible zeroes.

        no_div3 = actual_len // 3 #Floor division for getting only integeral part of division.

        min_range = no_div3 * 3
        max_range = min_range + 3

        return (min_range, max_range)

    def joinlist(self, a_list, typefunc):

        return typefunc("".join(a_list))

    def get_word(self):

        word_list = self._get_num_(self.num)

        for i in range( word_list.count("") ):

            word_list.remove("")

        word_num = " ".join(word_list)

        return word_num

    def _get_num_(self, num):

        str_num = str(num)

        if 0 <= num < 10:

            return [ self.list[0][str_num] ]

        elif 10 <= num < 20:

            return [ self.list[1][str_num] ]

        elif 20 <= num < 100:

            verblist = []

            num_list = self._get_list_(str_num)

            tens = self.list[1][num_list[0]]

            ones = self.list[0][num_list[1]]

            verblist.extend([tens, ones])

            return verblist

        elif 100 <= num < 1000:

            verblist = []

            num_list = self._get_list_(str_num)

            hundreds = self._get_num_( int(num_list[0]) ) + [ self.list[2] ] #Adding two lists.

            rest = self._get_num_( self.joinlist(num_list[1:], int) )

            verblist.extend(hundreds)
            verblist.extend(rest)

            return verblist

        else: #Conversion from 1000 to infinity is done here.

            verblist = []

            num_list = self._get_list_(str_num)

            zeroes_range = self.get_range(len(str_num)) #Getting new ranges in which no. of zeroes lies.

            slice_no = min(zeroes_range) * -1

            list_index = min(zeroes_range) / 3 + 2 #Gives an index of what to get from self.list i.e. thousand, million, billion etc.

            pre = self._get_num_( self.joinlist(num_list[:slice_no], int) ) + [ self.list[list_index] ] #Adding two lists.

            post = self._get_num_( self.joinlist(num_list[slice_no:], int))

            verblist.extend(pre)
            verblist.extend(post)

            return verblist
