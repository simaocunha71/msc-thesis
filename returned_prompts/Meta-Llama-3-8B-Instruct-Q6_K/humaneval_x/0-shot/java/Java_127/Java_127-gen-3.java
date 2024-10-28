Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int start1 = Math.max(interval1.get(0), interval2.get(0));
        int end1 = Math.min(interval1.get(1), interval2.get(1));
        if (start1 > end1) {
            return "NO";
        }
        int length = end1 - start1 + 1;
        if (isPrime(length)) {
            return "YES";
        } else {
            return "NO";
        }
    }

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

Explanation:

The problem is asking to find the intersection of two intervals and check if its length is a prime number. The intersection of two intervals is the set of numbers that are common to both intervals. The length of the intersection is the number of elements in the set.

First, we find the start and end of the intersection by taking the maximum of the start of the two intervals and the minimum of the end of the two intervals.

Then, we check if the start is greater than the end. If it is, it means the intervals do not intersect, so we return "NO".

Next, we calculate the length of the intersection by subtracting the start from the end and adding 1.

Finally, we check if the length is a prime number using a helper function `isPrime`. If it is, we return "YES", otherwise we return "NO".

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it is not a prime number. Otherwise, it is a prime number.