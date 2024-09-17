```
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left, right = left + 1, right - 1
    return "".join(s_list)
``` 

The function works by first converting the string to a list of characters. It then initializes two pointers, one at the start and one at the end of the list. It then iterates through the list, swapping the characters at the two pointers if they are both vowels, and moving the pointers towards the center of the list. This process continues until the pointers meet or cross, at which point the list is converted back to a string and returned. The function does not reverse the entire string, just the vowels, which is why it passes the test case where the input is "Python". 

The function also correctly handles uppercase and lowercase vowels, as well as the case where y is not a vowel, as per the unit test `assert reverse_vowels("Python") == "Python"`. 

Note: The time complexity of this function is O(n), where n is the length of the input string, because it makes a single pass through the string. The space complexity is O(n) as well, because it creates a new list of characters. 