def split_two_parts(nums, l):
    return (nums[:l], nums[l:])


# assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])
# print(split_two_parts([1,1,2,3,4,4,5,1],3))




"""
Write a function that takes in a string and a dictionary and returns True if the string contains all the keys from the dictionary, and False otherwise.
assert check_string_dict(“hello”, {“h”: 1, “e”: 1}) == True
assert check_string_dict(“hello”, {“h”: 1, “o”: 1}) == True
assert check_string_dict(“hello”, {“h”: 1, “l”: 1}) == True
assert check_string_dict(“hello”, {“h”: 1, “o”, “l”: 1}) == False
assert check_string_dict(“hello”, {“h”: 1, “o”, “n”: 1}) == False
"""

def check_string_dict(s, d):
    for k in d:
        if k not in s:
            return False
    return True


# assert check_string_dict(“hello”, {“h”: 1, “e”: 1}) == True
# assert check_string_dict(“hello”, {“h”: 1, “o”: 1}) == True
# assert check_string_dict(“hello”, {“h”: 1, “l”: 1}) == True
# assert check_string_dict(“hello”, {“h”: 1, “o”, “l”: 1}) == False
# assert check_string_dict(“hello”, {“h”: 1, “o”, “n”: 1}) == False
# print(check_string_dict(“hello”, {“h”: 1, “e”: 1}))

