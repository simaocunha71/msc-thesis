def all_Characters_Same(s):
    return len(set(s)) == 1

print(all_Characters_Same("python"))

"""
Explanation:
- The function takes a string as input.
- It converts the string to a set, which removes all duplicate characters.
- If the length of the set is 1, it means all characters in the string are the same. So it returns True.
- If the length of the set is greater than 1, it means there are at least two different characters in the string. So it returns False.
"""

# Task 2
