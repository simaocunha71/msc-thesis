```java
import java.util.*;
import java.lang.*;

class Solution {
    public int getMaxTriples(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = i * i - i + 1;
        }
        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if ((a[i] + a[j] + a[k]) % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```
This solution creates an array a of length n where each element is calculated as i * i - i + 1. Then it iterates through all possible triples (a[i], a[j], a[k]) where i < j < k and checks if their sum is a multiple of 3. If it is, it increments the count. Finally, it returns the count.