```java
import java.util.*;
import java.lang.*;

class Solution {
    public int largestDivisor(int n) {
        for (int i = n / 2; i >= 1; i--) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1;
    }
}
```
This solution iterates from n/2 down to 1, checking if each number divides n evenly. When it finds a number that divides n evenly, it returns that number. If it doesn't find any number that divides n evenly, it returns -1.