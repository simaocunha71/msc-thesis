The given intervals are closed. For each given interval, it is assumed that its start is less or equal its end. The intersection of the intervals is also a closed interval. If the two intervals don't intersect, return "NO". If the length of the intersection is a prime number, return "YES", otherwise, return "NO". Here is the Java code to solve this problem:

```java
import java.util.*;

public class Solution {
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
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

In the given code, we first calculate the start and end of the intersection interval. If the start is greater than the end, it means the two intervals don't intersect, so we return "NO". Then we calculate the length of the intersection interval. If the length is a prime number, we return "YES", otherwise, we return "NO". The isPrime function checks if a number is prime. It returns true if the number is prime, and false otherwise. The isPrime function uses a simple trial division method to check if a number is prime. It checks if the number is divisible by any number up to its square root, and if it is, it returns false. Otherwise, it returns true. This method is not very efficient for large numbers, but it is sufficient for the given problem. 