The Tribonacci sequence is a variation of the Fibonacci sequence where each term is the sum of the previous three terms, instead of the previous two. The base cases are tri(1) = 3 and tri(2) = 1. The recurrence relation is:

tri(n) = 1 + n/2, if n is even
tri(n) = tri(n-1) + tri(n-2) + tri(n+1), if n is odd

We can use a list to store the Tribonacci sequence and fill it up using the recurrence relation. Here is the Java solution:

```java
import java.util.*;

class Solution {
    public List<Integer> tri(int n) {
        List<Integer> tri = new ArrayList<>();
        tri.add(3); // tri(1) = 3
        if (n > 1) {
            tri.add(1); // tri(2) = 1
        }
        for (int i = 3; i <= n; i++) {
            if (i % 2 == 0) {
                tri.add(1 + i / 2); // tri(n) = 1 + n/2, if n is even
            } else {
                tri.add(tri.get(i-1) + tri.get(i-2) + tri.get(i-3)); // tri(n) = tri(n-1) + tri(n-2) + tri(n+1), if n is odd
            }
        }
        return tri;
    }
}
```

This solution works by initializing the list with the base cases tri(1) = 3 and tri(2) = 1. Then it uses a loop to fill up the list with the Tribonacci sequence using the recurrence relation. If n is even, the next term is 1 + n/2. If n is odd, the next term is the sum of the previous three terms. The final list is returned.