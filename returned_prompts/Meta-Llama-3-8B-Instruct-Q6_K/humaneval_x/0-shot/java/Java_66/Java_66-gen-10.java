The problem asks to create a function that takes a string as input and returns the sum of the ASCII codes of all uppercase characters in the string.

Here is the solution in Java:

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

This function iterates over each character in the input string. If the character is uppercase (checked using `Character.isUpperCase(c)`), it adds the ASCII value of the character to the sum. The sum is then returned as the result.

For example, if the input string is "abAB", the function will iterate over each character: 'a' is lowercase, 'b' is lowercase, 'A' is uppercase, and 'B' is uppercase. The ASCII values are 97, 98, 65, and 66, respectively. The sum is 97 + 98 + 65 + 66 = 326. However, the problem asks for the sum of the ASCII codes of the uppercase characters only, which is 65 + 66 = 131. Therefore, the function will return 131.