The problem is asking to write a function that takes a string as input and returns the sum of the ASCII codes of all uppercase characters in the string.

Here is the solution:
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
This function iterates over each character in the input string, checks if it is an uppercase character using the `Character.isUpperCase()` method, and if it is, adds its ASCII code to the sum. Finally, it returns the sum.

For example, if the input string is "abAB", the function will iterate over the characters 'a', 'b', 'A', and 'B'. It will add the ASCII codes of 'A' and 'B' to the sum, which are 65 and 66 respectively. So, the function will return 131.