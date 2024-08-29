def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)

print(reverse_vowels("Python"))  # should return "Python"

# Solution 2
def reverse_vowels(s):
    vowels = "aeiou"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i].lower() not in vowels:
            i += 1
        elif s[j].lower() not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return "".join(s)

print(reverse_vowels("Hello"))  # should return "Holle"
"""
In this problem, we are asked to write a Python function that will reverse the vowels in a given string. We will convert the string into a list because strings in Python are immutable, so we can't modify the string in-place. 

We will use two pointers method to solve this problem. Initially, one pointer will start from the beginning of the string and the other will start from the end of the string. We will move both pointers towards the center of the string. If both pointers point to vowels, we will swap them. If the first pointer points to a consonant, we will move it forward and if the second pointer points to a consonant, we will move it backward. We will continue this process until the two pointers meet. At the end, the list will have the vowels reversed and the consonants in their original positions. We will join the list back into