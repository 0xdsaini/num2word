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

def separate(word_num, output_sep):

    if output_sep == 'csv':
        return word_num

    if output_sep == 'lsv':
        return "\n".join( word_num.split(", ") ) #Joining with newline separation.

    elif output_sep == 'lscev':
        return ",\n".join( word_num.split(", ") ) #Joining with newline separation.
