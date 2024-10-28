```java
public int digitSum(String s) {
    int sum = 0;
    for (char c : s.toCharArray()) {
        if (Character.isUpperCase(c)) {
            sum += (int) c;
        }
    }
    return sum;
}
```
Explanation:
The function `digitSum` takes a string `s` as input and returns the sum of the ASCII codes of the upper case characters in the string.

We iterate through each character `c` in the string using a for-each loop. For each character, we check if it is an upper case character using the `Character.isUpperCase` method. If it is an upper case character, we add its ASCII code to the sum using the expression `(int) c`.

Finally, we return the sum.

This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), as we only use a constant amount of space to store the sum.