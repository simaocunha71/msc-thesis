
def reverse_delete(s,c):
    for ch in c:
        s = s.replace(ch, "")
    return (s, s == s[::-1])

print(reverse_delete("abcde", "ae"))
print(reverse_delete("abcdef", "b"))
print(reverse_delete("abcdedcba", "ab"))

# Output:
# ('bcd', False)
# ('acdef', False)
# ('cdedc', True)

Explanation:

The function reverse_delete(s,c) is defined which takes two arguments, a string s and a string c. 
Then the function iterates through each character in the string c and replaces all instances of the character in the string s.
After that, it returns a tuple containing the result string and a boolean value indicating whether the result string is a palindrome or not.
The boolean value is True if the result string is equal to its reverse and False otherwise.
We then call this function with the given examples and print the output.

The string s is reversed using s[::-1] and then compared with the original string to check if it is a palindrome. 
If they are equal, then the string is a palindrome and the function returns True, otherwise it returns False. 
This is done in the form of a tuple (s, s == s[::-1]). 

The time complexity of this solution is O(n*m), where n is the length of the string s and m is the length of the string c. 
This is because for every character in c, we are replacing all instances of that character in s. 
So, in the worst case, we are doing n replacements for each character in c. 
So, the time complexity is O(n*m).
The space complexity is O(n), as we are storing the result string.
"""

# 2. Write a Python program that takes a string as input and returns the frequency of each character in the string.

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else: