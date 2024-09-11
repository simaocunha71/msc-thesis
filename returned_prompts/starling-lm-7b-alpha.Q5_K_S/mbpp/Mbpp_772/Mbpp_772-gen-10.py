def remove_length(s, k):
    return " ".join(filter(lambda x: len(x) != k, s.split()))


# Another way
def remove_length_another(s, k):
    return " ".join([i for i in s.split() if len(i) != k])


print(remove_length('The person is most value tet', 3))
print(remove_length_another('The person is most value tet', 3))


"""
Runtime: O(n), n is the length of the input string
Space: O(n)
"""

# This solution uses Python built-in function `filter` and `join` which have time complexity O(n) and O(1) respectively.
# The time complexity of this solution is O(n).
# The auxiliary space of this solution is O(n) which is the worst-case scenario of the `join` function.
"""
In the worst-case scenario, all the characters in the given string are separated by spaces and have length k.
In this scenario, the `filter` function will filter out all the characters, and the `join` function will concatenate all the remaining characters back to the string.
As a result, the space complexity of this solution is O(n).
"""

"""
Alternative Solution

def remove_length(s, k):
    return " ".join(s.split(sep=" ")[::2])


# Another way
def remove_length_another(s, k):
    return " ".join(s.split(sep=" ")[1::2])
"""

"""
This solution has a time complexity of O(n) and a space complexity of O(1) as it only uses basic string manipulation operations.
"""

"""
This solution splits the given string into a list of words using the `split` method with space as the separator, then it uses the slicing operation to remove every other word from the list, and finally it joins the remaining words back to the string using the `join` method.
"""

"""
The time complexity of this solution is O(n) because it splits the string into a list of words, which takes O(n) time, and