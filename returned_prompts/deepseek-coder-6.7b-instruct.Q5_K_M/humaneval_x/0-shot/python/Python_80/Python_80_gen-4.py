
def is_happy(s):
    if len(s) < 3:
        return False
    else:
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) != 3:
                return False
        return True

print(is_happy('a'))         # False
print(is_happy('aa'))        # False
print(is_happy('abcd'))      # True
print(is_happy('aabb'))      # False
print(is_happy('adb'))       # True
print(is_happy('xyy'))       # False

The function works by first checking if the length of the string is less than 3. If it is, it returns False. Otherwise, it goes through the string and checks if there are 3 consecutive characters that are all different. It does this by converting the 3 characters into a set, and if the length of the set is not 3, it returns False. If it goes through the entire string without finding any non-distinct triplets, it returns True.

This function assumes that the input string is composed of only lowercase English letters. If the input string can contain uppercase English letters, digits, or special characters, the function needs to be modified to handle these cases.

Note: The time complexity of this function is O(n), where n is the length of the string. This is because it has to go through each character of the string once. The space complexity is also O(n), because in the worst case (when all characters are different), the set created in each iteration of the loop has to store all characters.

Also note that this function uses Python's built-in set data structure, which is implemented as a hash table. Therefore, the time complexity of the set operations (add, remove, and in) is O(1) on average, assuming the hash function is good and the table is not too full.

In summary, this function should be efficient and can handle most use cases.

```





























































