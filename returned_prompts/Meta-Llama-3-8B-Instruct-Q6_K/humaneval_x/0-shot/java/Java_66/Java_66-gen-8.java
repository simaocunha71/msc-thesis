The problem is asking to write a function that takes a string as input and returns the sum of the ASCII codes of all uppercase letters in the string.

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

This function uses a for-each loop to iterate over each character in the input string. It uses the `Character.isUpperCase` method to check if the character is uppercase. If it is, it adds the ASCII value of the character to the sum. Finally, it returns the sum.