The problem is asking to write a function that takes a string as input and returns the sum of the ASCII codes of all the uppercase characters in the string.

Here's the solution in Java:

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

This function works by iterating over each character in the input string. If the character is uppercase (checked using the `Character.isUpperCase` method), its ASCII code is added to the sum. The sum is then returned at the end of the function.

For example, if the input string is "abAB", the function will iterate over each character, and the uppercase characters 'A' and 'B' will have their ASCII codes (65 and 66 respectively) added to the sum. The sum will be 131, which is the correct result.