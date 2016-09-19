#1.4 Palindrome Permutation: Given a string, write a function to check if tis a permutation of a palindrome.

from types import *

def isPalindrome(a_str):
    assert type(a_str) is StringType, "Input %s: not String!" %a_str
    if len(a_str) == 1:
        return True
    else:
        # create a dictionary of characters, to count number of times of occurence.
        dict_char_in_string = {}
        for a_chr in a_str:
            if a_chr != ' ':
                if a_chr not in dict_char_in_string.keys():
                    dict_char_in_string[a_chr] = 1
                else:
                    dict_char_in_string[a_chr] = dict_char_in_string[a_chr] + 1
            else: # a_chr == " "
                pass

        # count if char occurs even number of times or odd
        num_odd_appearances =  sum([xint%2 for xint in dict_char_in_string.values()])
        if num_odd_appearances > 1:
            return False
        else:
            return True


if __name__=="__main__":
    a_str = raw_input("Enter string with spaces\n")

    if (isPalindrome(a_str)):
        print("True: Is permuation of Palindrome")
    else:
        print("False: Not a permuation of palindrome")
