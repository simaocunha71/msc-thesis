Here is a Java solution for the problem:

```java
public int fizzBuzz(int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            String num = Integer.toString(i);
            for (int j = 0; j < num.length(); j++) {
                if (num.charAt(j) == '7') {
                    count++;
                }
            }
        }
    }
    return count;
}
```

This solution iterates over all numbers less than `n` and checks if they are divisible by 11 or 13. If they are, it converts the number to a string and counts the occurrences of the digit '7'. The count is then returned as the result.