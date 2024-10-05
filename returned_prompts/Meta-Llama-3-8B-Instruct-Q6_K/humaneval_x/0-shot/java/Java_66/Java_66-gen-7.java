The problem is asking to find the sum of the ASCII values of all uppercase characters in a given string. 

Here is a simple Java solution for this problem:

```java
public int digitSum(String s) {
    int sum = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (Character.isUpperCase(c)) {
            sum += (int) c;
        }
    }
    return sum;
}
```

In this solution, we iterate over each character in the string. If the character is an uppercase letter (checked using the `Character.isUpperCase` method), we add its ASCII value to the sum. The ASCII value of a character is obtained by casting the character to an integer using the `(int)` cast. 

This solution works for all the examples provided in the problem statement. For example, for the input "abAB", the sum of the ASCII values of the uppercase characters is 131 (A=65, B=66). Similarly, for the input "abcCd", the sum is 67 (C=67, D=68). 

Note that this solution assumes that the input string contains only ASCII characters. If the input string can contain non-ASCII characters, additional handling would be needed to correctly handle these characters. 