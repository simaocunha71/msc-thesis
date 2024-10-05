        int count = 0;
        for (int i = 11; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += countDigit(i, 7);
            }
        }
        return count;
    }

    private static int countDigit(int number, int digit) {
        int count = 0;
        while (number > 0) {
            if (number % 10 == digit) {
                count++;
            }
            number = number / 10;
        }
        return count;
    }
}


A: The provided solution does not work correctly as it counts the occurrences of 7 in the number divisible by 11 or 13. In this case, the countDigit function counts the digit 7 in the number, but it doesn't check whether the number is divisible by 11 or 13.

Here is a corrected solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizzBuzz(50)
    • 0
    >>> fizzBuzz(78)
    • 2
    >>> fizzBuzz(79)
    • 3
      */
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 11; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += countDigit(i, 7);
            }
        }
        return count;
    }

    private static int countDigit(int number, int digit) {
        int count = 0;
        while (number > 0) {
            if (number % 10 == digit) {
                count++;
            }
            number = number / 10;
        }
        return count;
    }
}
```

In this solution,