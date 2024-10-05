```java
import java.util.*;

class Solution {
    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        int[] fibfib = new int[n + 1];
        fibfib[1] = fibfib[2] = 0;
        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }
        return fibfib[n];
    }
}
```
This solution creates an array of size n + 1 to store the values of the fibfib sequence. It initializes the first three elements as 0 and 1. Then it calculates the rest of the elements using the formula fibfib(i) = fibfib(i-1) + fibfib(i-2) + fibfib(i-3). Finally, it returns the nth element of the array. This solution has a time complexity of O(n) and a space complexity of O(n).