def find_substring(lst, s):
    for i in range(len(lst)):
        if s in lst[i]:
            return True
    return False


# Driver code
print(find_substring(["red", "black", "white", "green", "orange"],"ack"))


"""
The time complexity of the above solution is O(n*m), where n is the length of the list of strings, and m is the maximum length of the strings in the list.
The space complexity of the solution is O(1), as no additional space is used.
"""

