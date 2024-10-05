```java
public boolean isHappy(String s) {
    if (s.length() < 3) return false;
    for (int i = 0; i < s.length() - 2; i++) {
        if (s.charAt(i) == s.charAt(i + 1) || s.charAt(i) == s.charAt(i + 2) || s.charAt(i + 1) == s.charAt(i + 2)) {
            return false;
        }
    }
    return true;
}
```
Explanation:
The problem is asking to check if a given string is happy or not. A string is happy if its length is at least 3 and every 3 consecutive letters are distinct. 

We start by checking if the length of the string is less than 3. If it is, we return false because a happy string must have a length of at least 3.

Then, we iterate over the string using a for loop. We check if the current character and the next two characters are the same. If they are, we return false because it means that the string is not happy.

If the loop finishes without returning false, it means that every 3 consecutive letters in the string are distinct, so we return true. This means that the string is happy. 

For example, if the input is "abcd", the function will return true because every 3 consecutive letters are distinct. If the input is "aa", the function will return false because the first two characters are the same. If the input is "aabb", the function will return false because the last two characters are the same. If the input is "adb", the function will return true because every 3 consecutive letters are distinct. If the input is "xyy", the function will return false because the last two characters are the same. 

This solution has a time complexity of O(n) where n is the length of the input string. This is because we are iterating over the string once. The space complexity is O(1) which means that the space used does not change with the size of the input string. This is because we are not using any data structures that scale with the size of the input string. 