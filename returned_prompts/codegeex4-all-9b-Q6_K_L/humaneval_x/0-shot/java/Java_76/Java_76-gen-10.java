Here is the Java code to solve the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        if (x == 1) {
            return true;
        }
        if (n == 1) {
            return false;
        }
        int power = n;
        while (power < x) {
            power *= n;
        }
        return power == x;
    }
}
```

Explanation:

First, we check if the number is 1. If it is, then it is a simple power of any number, so we return true.

Next, we check if the number is a simple power of 1. If it is, then it is not a simple power of any number other than itself, so we return false.

Then, we start a loop that multiplies the number by itself until it is greater than or equal to the input number. If the result is equal to the input number, then the input number is a simple power of the starting number, so we return true. Otherwise, we return false.