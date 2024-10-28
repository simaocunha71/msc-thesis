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
    return "".join(s_list)  # or return "".join(s_list) if you want to keep the original string

# Test case
assert reverse_vowels("Python") == "Python", f"Expected reverse_vowels('Python') to return 'Python', but got {reverse_vowels('Python')}"
print("All test cases pass")  # If all test cases pass, this will be printed
```


The solution iterates over the string from both ends, checking if the characters are vowels. If they are, it swaps them. If not, it moves the pointer towards the center of the string. The function returns the modified string. 

The unit test checks if the function correctly returns the original string when all characters are not vowels. If the function returns any value other than "Python", the test fails, indicating that the function is not working correctly. 

The test case `assert reverse_vowels("Python") == "Python"` ensures that the function does not modify the string when all characters are not vowels. This is because the problem statement does not specify what to do when all characters are not vowels, and it's reasonable to assume that the function should leave the string unchanged in this case. 

If the test case passes, it means that the function is working correctly, and the output will be "All test cases pass". If the test case fails, it means that the function is not working correctly, and the output will be an error message indicating which test case failed. 





# Python code to reverse only the vowels of a given string
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else