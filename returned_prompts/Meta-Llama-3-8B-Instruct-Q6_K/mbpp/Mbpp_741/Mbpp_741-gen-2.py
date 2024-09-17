```
def all_Characters_Same(s):
    return len(set(s)) == 1
```
This function works by converting the string into a set, which is an unordered collection of unique elements. If the length of the set is 1, it means all characters in the string are the same. Otherwise, it means there are different characters in the string. The function returns False when there are different characters. 

For example, the string "python" has different characters, so the function will return False. On the other hand, the string "aaaa" has the same characters, so the function will return True. 

The unit test `assert all_Characters_Same("python") == False` ensures that the function works correctly for the string "python".  If the function is working correctly, this unit test will not throw an AssertionError. 

The time complexity of this function is O(n), where n is the length of the string. This is because the function has to iterate over the entire string to convert it into a set. The space complexity is also O(n), as the function has to store all characters in the set. 