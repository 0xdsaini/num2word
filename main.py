#!/usr/bin/env python

class verbal_num(object):

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

    def _get_list_(self, num):
        """Returns a list of one digit numbers."""

        return [x for x in str(num)]

    def joinlist(self, a_list, typefunc):

        return typefunc("".join(a_list))

    def get_num(self):

        return self._get_num_(num)

    def _get_num_(self, num):

        str_num = str(num)

        if 0 <= num < 10:

            return self.list[0][str_num]

        if 10 <= num < 20:

            return self.list[1][str_num]

        if 20 <= num < 100:

            verbnum = ""

            num_list = self._get_list_(str_num)

            tens = self.list[1][num_list[0]]

            ones = self.list[0][num_list[1]]

            verbnum = tens + " " + ones

            return verbnum

        if 100 <= num < 1000:

            verbnum = ""

            num_list = self._get_list_(str_num)

            hundreds = self._get_num_( int(num_list[0]) ) + " " + self.list[2]

            rest = self._get_num_( self.joinlist(num_list[1:], int) )

            verbnum = hundreds + " " + rest

            return verbnum

        if 1000 <= num < 1000000:

            verbnum = ""

            num_list = self._get_list_(str_num)

            thousands = self._get_num_( self.joinlist(num_list[:-3], int) ) + " " + self.list[3]

            rest = self._get_num_( self.joinlist(num_list[-3:], int))

            verbnum = thousands + " " + rest

            return verbnum

        if 1000000 <= num < 100000000:

            verbnum = ""

            num_list = self._get_list_(str_num)

            millions = self._get_num_( self.joinlist(num_list[:-6], int) ) + " " + self.list[4]

            rest = self._get_num_( self.joinlist(num_list[-6:], int))

            verbnum = millions + " " + rest

            return verbnum

num = input("Enter Number : ")
a = verbal_num(num)

print a.get_num()
