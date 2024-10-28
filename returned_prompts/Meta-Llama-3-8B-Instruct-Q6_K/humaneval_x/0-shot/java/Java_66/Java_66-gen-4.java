The problem is asking for the sum of the ASCII values of all uppercase characters in a given string.

Here is a simple Java solution for this problem:

```java
import java.util.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;
        for (char c : s.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sum += c;
            }
        }
        return sum;
    }
}
```

In this solution, we iterate over each character in the string using a for-each loop. We check if the character is uppercase using the `Character.isUpperCase()` method. If it is, we add its ASCII value to the sum. Finally, we return the sum.

This solution assumes that the input string is not null. If the input string can be null, you should add a null check at the beginning of the method:

```java
public int digitSum(String s) {
    if (s == null) {
        return 0;
    }
    int sum = 0;
    for (char c : s.toCharArray()) {
        if (Character.isUpperCase(c)) {
            sum += c;
        }
    }
    return sum;
}
```



