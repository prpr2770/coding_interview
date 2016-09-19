#1.3 Write a method to replace all spaces in a string with '%20'.

"""Assume: String has sufficient space at end to hold the additional characters
and that you're given the true length of the string. """

from types import *

def urlify(a_str, b_int):
    assert type(a_str) is StringType, "Input 1 not String!"
    assert type(b_int) is IntType, "Input 2 is not Integer!"

    count = 0
    result_str = ''
    for a_chr in a_str:
        if a_chr != ' ':
            count = count + 1
            result_str = result_str + a_chr
        else:
            if count > 0 & count <= b_int:
                result_str = result_str + '%20'
            else:
                pass

    return result_str


if __name__=="__main__":
    a_str = raw_input("Enter string with spaces\n")
    b_int = int(raw_input("Enter number of non-space characters in string\n"))

    print(urlify(a_str,b_int))
