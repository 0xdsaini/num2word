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

"""Integers to Verbal numbers converter i.e. 100 to 'One Hundred'"""

from sys import argv
from libn2w import Verbal

USAGE = """n2w: missing operand
Try 'n2w --help' for more information."""

HELP = """Usage: n2w NUMBER
   or: n2w OPTIONS

      --help     display this help and exit
      --version  output version information and exit

Print the value of NUMBER in English words to standard output."""

def arg_verify(arg_list):

    if len(arg_list) > 1:
        return 3 # Arguments are more than 2.

    elif len(arg_list) == 1:

        try:
            num = int(arg_list[0])
            return num

        except ValueError:
            return 4 # Number argument is not number

def contains(compare_list, allowed_elements, strategy='or'):

    if strategy=='and': #Checks whether compare_list is a subset of allowed_elements.

        if set(compare_list).issubset(set(allowed_elements)):
            return True
        else:
            return False

    elif strategy=='or': #Return True as soon as any element from compare_list is in the allowed_elements.

        for element in compare_list:

            if element in allowed_elements:
                return True

        return False

def num2word(num):

    Verbal_obj = Verbal(num)

    verbal_num = Verbal_obj.get_num()

    del Verbal_obj

    return verbal_num

# Main starts here:-

if len(argv) == 1: #If no command-line argument is given

    print USAGE
    exit(2)

if len(argv) > 1:

    if contains(argv[1:], ['--help', '-h']):

        print HELP
        exit(0)

    elif arg_verify(argv[1:]) == 3:

        print "Too many arguments."
        exit(3)

    elif arg_verify(argv[1:]) == 4:

        print "Invalid Argument, only decimal number is allowed."
        exit(4)

    else:
        num = arg_verify(argv[1:])

print num2word(num)

