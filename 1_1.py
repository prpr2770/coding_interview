# 1.1 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def isUnique_characters(a_str):
	char_dict = {}
	for a_char in a_str:
		if a_char not in char_dict:
			char_dict[a_char] = 1
		else:
			char_dict[a_char] = char_dict[a_char] + 1

	print(char_dict)
	if len(char_dict.keys()) != sum(char_dict.values()):
		return False
	else:
		return True

if __name__=="__main__":
	a_str = raw_input("Enter string\n")
	if(isUnique_characters(a_str)):
		print("True: string contains unique char")
	else:
		print("False: string contains repeated char")
