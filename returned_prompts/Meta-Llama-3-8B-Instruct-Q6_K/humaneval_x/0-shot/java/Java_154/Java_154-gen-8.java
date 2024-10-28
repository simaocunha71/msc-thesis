```java
public boolean cycpatternCheck(String a, String b) {
    int lenA = a.length();
    int lenB = b.length();
    for (int i = 0; i < lenA; i++) {
        String temp = a.substring(i) + a.substring(0, i);
        if (temp.contains(b)) {
            return true;
        }
    }
    return false;
}
```
The idea is to create a temporary string by rotating the first string and check if the second string is present in the temporary string. If it is, return true. If it is not, return false. 

For example, if the first string is "abcd" and the second string is "abd", the function will create the following temporary strings: "abcd", "bcd", "cd", "d". It will check if "abd" is present in each of these strings. Since "abd" is not present in any of these strings, the function will return false.

If the first string is "hello" and the second string is "ell", the function will create the following temporary strings: "hello", "ello", "llo", "lo", "o". It will check if "ell" is present in each of these strings. Since "ell" is present in the second temporary string, the function will return true.

This solution has a time complexity of O(n*m), where n is the length of the first string and m is the length of the second string. This is because in the worst case, we are checking if the second string is present in the first string, which takes O(n*m) time. The space complexity is O(1), which is the space required to store the temporary strings. 