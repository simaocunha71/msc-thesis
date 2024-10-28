```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    A simple program which should return the value of x if n is
    a prime number and should return the value of y otherwise.

    Examples:
    for xOrY(7, 34, 12) == 34
    for xOrY(15, 8, 5) == 5
     */
    public int xOrY(int n, int x, int y) {
        if (n <= 1) {
            return y;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return y;
            }
        }
        return x;
    }
}
```