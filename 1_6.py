#1.6 String Compression:
"""
Implement a method to perform basic string compression using the coutns of repeated characters.

"""
from types import *


def get_compressed_string(a_str):
    res_str = '' # tracks final result string to be printed.
    present_new_chr = '' # tracks present character pointer
    present_chr_count = 0 # tracks number of times the character has been repeated.

    if len(a_str) > 0:
        # idx ==0
        present_new_chr = a_str[0]
        present_chr_count = 1
        res_str = res_str + a_str[0]

        for idx in xrange(1,len(a_str)):
            if a_str[idx] == present_new_chr:
                present_chr_count = present_chr_count + 1
            else:
                present_new_chr = a_str[idx] # reset inital value
                res_str = res_str + str(present_chr_count) + present_new_chr
                present_chr_count = 1 # reset counter
        res_str = res_str + str(present_chr_count)
        return res_str
    else: # if input was empty
        return a_str

if __name__=="__main__":
    a_str = raw_input("Enter string with spaces\n")

    res_str = get_compressed_string(a_str)
    print("Compressed string: %s"% res_str)

    if len(res_str) == len(a_str):
        print("Final adopted value: %s" % a_str)
