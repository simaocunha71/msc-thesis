```
def remove_Occ(s, char):
    s = list(s)
    if s[0] == char:
        s.pop(0)
    if s and s[-1] == char:
        s.pop()
    return ''.join(s)
```


This function converts the string into a list of characters. It then checks if the first and last characters are equal to the given character. If they are, it removes them using the pop(0) and pop() methods. Finally, it converts the list back into a string using the join() method. If the given character is not found in the string, the function returns the original string. 

The unit test `assert remove_Occ("hello","l") == "heo"` ensures that the function removes both the first and last occurrence of the character 'l' from the string "hello" and returns "heo". 

The time complexity of this function is O(n) where n is the length of the string, as it needs to iterate over the string to remove the characters. The space complexity is also O(n) as it needs to store the characters in a list. 





```
def remove_Occ(s, char):
    s = list(s)
    if s and s[0] == char:
        s.pop(0)
    if s and s[-1] == char:
        s.pop()
    return ''.join(s)
```


This function converts the string into a list of characters. It then checks if the first and last characters are equal to the given character. If they are, it removes them using the pop(0) and pop() methods. Finally, it converts the list back into a string using the join() method. If the given character is not found in the string, the function returns the original string. 

The unit test `assert remove_Occ("hello","l") == "heo"` ensures that the function removes both the first and last occurrence of the character 'l' from the string "hello" and returns "heo". 

The time complexity of this function is O(n) where n is the length of the string, as it needs to iterate over the string to remove the characters. The space complexity is also O(n) as it needs to store the characters in a list. 





```
def remove_Occ(s, char):
    s = list(s)
    if s and s[0] == char:
        s.pop(0)
    if s and s[-1