def count_char_position(s):
    return sum(ord(c) - ord('a') + 1 == i + 1 for i, c in enumerate(s.lower()))


# Alternative solution using zip
def count_char_position_zip(s):
    return sum(c == alphabet[i] for i, c in enumerate(s.lower()) for alphabet in 'abcdefghijklmnopqrstuvwxyz')


# Alternative solution using zip
def count_char_position_zip(s):
    return sum(c == alphabet[i] for i, c in enumerate(s.lower()) for alphabet in 'abcdefghijklmnopqrstuvwxyz')

"""
>>> count_char_position("xbcefg")
2
>>> count_char_position("abcdefgh")
7
>>> count_char_position("aaaccbb")
6
>>> count_char_position("qwertyuiop")
0
>>> count_char_position("zxcvbnmlkjhg")
6
"""



"""



"""




# Python3 Program to Count the
# Number of Characters at same
# index as in alphabets

# Function to count the number
# of characters at same index
# as in alphabets
def count_char_position(s):

	# Initialize count
	count = 0;

	# Traverse the string
	for i in range(len(s)):

		# If characters are same
		# as alphabets at same index
		if (ord(s[i]) - ord('a') + 1 == i + 1):

			# Increment count
			count += 1;

	# Return count
	return count;

# Driver Code
s = "xbcefg"
print(count_char_position(s))
```