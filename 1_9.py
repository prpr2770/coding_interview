# 1.9 String Rotation:

"""
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
"""

def isSubstring(a_str,b_str):
	if len(a_str) != len(b_str):
		print("Unequal lengths")
		return False
	elif a_str == b_str:
		print("Identity rotation")
		return True
	else:
		for idx in xrange(0,len(a_str)):
			c_str = a_str[idx:] + a_str[:idx]
			if c_str == b_str:
				return True
		print("Not a rotated permutation!")
		return False

if __name__=="__main__":
	a_str = raw_input("Enter string 1:\n")
	b_str = raw_input("Enter string 2:\n")

	if(isSubstring(a_str,b_str)):
		print("True: strings are rotated permutations")
	else:
		print("False: strings are NOT rotated permutations")
