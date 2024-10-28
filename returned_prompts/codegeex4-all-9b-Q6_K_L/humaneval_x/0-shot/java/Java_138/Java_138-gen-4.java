```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isEqualToSumEven(int n) {
        // A number can be written as the sum of exactly 4 positive even numbers
        // if and only if the number is at least 8.
        return n >= 8;
    }
}
```