
def number_of_substrings(s):
    n = len(s)
    return n*(n+1)//2

print(number_of_substrings("abc"))

# This program works by simply counting the number of substrings. 
# For the string of length n, there are n(n+1)/2 non-empty substrings. 
# This is due to the fact that for each character in the string, 
# there are (n-i) substrings where i is the index of the character (0-indexed). 
# The sum of these numbers from i=0 to i=n-1 gives n*(n+1)/2.
<jupyter_output>
6
<jupyter_text>
Question 2
<jupyter_code>
