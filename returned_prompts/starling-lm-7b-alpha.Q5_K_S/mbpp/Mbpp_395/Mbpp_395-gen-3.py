def first_non_repeating_character(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s:
        if d[i] == 1:
            return i
    return None

# Test
print(first_non_repeating_character("abcabc"))  # None
print(first_non_repeating_character("abcdefghijklmnopqrstuvwxyz"))  # a
print(first_non_repeating_character("qwertyuiopasdfghjklzxcvbnm"))  # q



def first_non_repeating_character(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in s:
        if d[i] == 1:
            return i
    return None

# Test
print(first_non_repeating_character("abcabc"))  # None
print(first_non_repeating_character("abcdefghijklmnopqrstuvwxyz"))  # a
print(first_non_repeating_character("qwertyuiopasdfghjklzxcvbnm"))  # q


"""
In the above code, we create a dictionary 'd' to store the count of each character in the given string 's'.
Then we iterate through the string 's' again to check if the count of the character is equal to 1, which means it's the first non-repeated character, and we return it.
If no non-repeated character is found, we return None.
"""

"""
The time complexity of this solution is O(n), where n is the length of the string 's'. This is because we iterate through the string twice.
The space complexity is also O(n) since we use a dictionary to store the count of each character in the string.
"""

"""
Alternative Solution:
We can use a set to keep track of