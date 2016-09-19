#1.5 One Away: There are 3 types of edits that can be performed on strings: insert, remove, replace : a character!
# Given two stings, write a functiont o check if they are one edit, or zero edits away.

from types import *

def less_one_edit_away(a_str, b_str, num_prev_mismatches):
    assert type(a_str) is StringType, "Input 1: %s is not string!" % a_str
    assert type(b_str) is StringType, "Input 1: %s is not string!" % b_str

    if num_prev_mismatches > 1:
        return False
    elif abs(len(a_str) - len(b_str)) > 1:  #length differ by >1
        return False
    elif len(a_str) == 1 or len(b_str) ==1: # either of strings has only one char
        if len(set(a_str).intersection(set(b_str))) == 1:
            return True
        else:
            return False
    else: # lengths differ by 1, and both strings are > 1 char long!
        if a_str[0] != b_str[0]:
            return less_one_edit_away(a_str[1:], b_str[1:], num_prev_mismatches + 1)
        else:
            return less_one_edit_away(a_str[1:], b_str[1:], num_prev_mismatches)



if __name__=="__main__":
    a_str = raw_input("Enter string with spaces\n")
    b_str = raw_input("Enter string with spaces\n")

    if (less_one_edit_away(a_str,b_str, 0)):
        print("True: %s is one-edit-away from %s" % (a_str, b_str))
    else:
        print("False: %s is NOT one-edit-away from %s" % (a_str, b_str))
