#1.2 Check Permutation: Given two stings write a method to decide if one is a permutation of the other.

from types import *

def isPermutation(a_str, b_str):
    assert type(a_str) is StringType, "Input Data 1: %s, is not a string" %a_str
    assert type(b_str) is StringType, "Input Data 2: %s, is not a string" %a_str

    if len(a_str) != len(b_str):
        return False
    else:
        if ''.join(sorted(a_str)) == ''.join(sorted(b_str)):
            return True
        else:
            return False


if __name__ == "__main__":
    a_str = raw_input("Enter first string\n")
    b_str = raw_input("Enter second string\n")

    if(isPermutation(a_str, b_str)):
        print("True: Permutation of each other")
    else:
        print("False: Not permutations of each other")
