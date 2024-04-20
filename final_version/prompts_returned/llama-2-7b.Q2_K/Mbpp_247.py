"""
Write a function to find the length of the longest palindromic subsequence in the given string.
assert lps("TENS FOR TENS") == 5
"""

def palindrome(s):
    if len(s)<2: # no need to check if s is longer than 1, then we just print the empty str and return
        print('No substrings')
        return
    elif len(s)>=3 and (s[0:2]==s[len(s)-2:]): # check if the first character in the string is a letter or number and same goes for last character, it is enough to check only two characters at a time and then check every 2 chars
        longest_palindromic_subsequence = ''.join([str(i) for i in s[0:2]]) # get the first 2 letters of the string, then form a str out of them with '.join' function.
        if len(longest_palindrome)>len(s):
            longest_palindromic_subsequence = ''.join([str(i) for i in s[3:5]]) # check the next 2 letters, then find the next bigger number and use it to make another string with 5 letteres long.
    if len(longest_palindrome)>1: # check if the subsequence is longer than 1 character
        # if length of longest palindromic sequence is larger than the passed string, print 'Not possible'
        for i in range(3,len(s),2):
            if len(longest_palindrome)>=1:
                # check if the current letter is not a letter or number (so it will be a palin in subsequence) and check if next letter isn't either (so we will have a full palindromic sequence)
                if (not ((len(longest_palindrome)>=2 and len(longest_palindrome[0:2])>=1 and int(longest_palindrome[0:2], base=16)%2==1 ) and ( not (len(longest_palindrome-i+1)>=2 and len(longest_palindrome-i+1,base=16)%2 == 1 or not int(longest_palindrome-i+1, base=16) % 2 == 1))):
                    if (int(s[i], base=