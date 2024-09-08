def unique_Element(lst):
    return len(set(lst)) <= 1

print(unique_Element([1,1,1]))
print(unique_Element([1,2,3]))
print(unique_Element([1]))
print(unique_Element([]))

"""
This function works by converting the list into a set, which automatically removes duplicate elements. It then checks if the length of the set is less than or equal to 1. If the length is less than or equal to 1, this means that all elements in the list were the same, so the function returns True. If the length is greater than 1, this means that there were multiple distinct elements in the list, so the function returns False.
"""
<jupyter_output>
True
False
True
True
<jupyter_text>
Q2:Write a Python function to check if a given list is a palindrome or not. A palindrome is a sequence that reads the same backwards as forwards.
<jupyter_code>
def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1,2,3,2,1]))
print(is_palindrome([1,2,3,4,5]))
<jupyter_output>
True
False
<jupyter_text>
Q3:Write a Python function that takes a list of strings and returns a list of strings that are anagrams of each other. Two strings are anagrams if they contain the same characters but in a different order.
<jupyter_code>
def find_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return [words for words in anagrams.values() if len(words) > 1]

print(find_anagrams(["cat", "dog", "tac", "god", "good",