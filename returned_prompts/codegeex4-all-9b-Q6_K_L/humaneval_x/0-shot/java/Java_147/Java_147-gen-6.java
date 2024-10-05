Here is the Java code for the problem:

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
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
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
This code first creates the array a as described in the problem. Then, it iterates through all possible triples (i, j, k) where i < j < k. If the sum of the elements at these indices in array a is divisible by 3, it increments the count. Finally, it returns the count.