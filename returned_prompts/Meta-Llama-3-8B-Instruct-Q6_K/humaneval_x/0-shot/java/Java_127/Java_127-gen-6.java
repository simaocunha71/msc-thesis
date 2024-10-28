This is a Java code solution for the problem. It first calculates the intersection of the two intervals, then checks if the length of the intersection is a prime number. If it is, the method returns "YES", otherwise it returns "NO".

```java
import java.util.*;

class Solution {
    public String intersection(List<Integer> interval1, List<Integer> interval2) {
        int start = Math.max(interval1.get(0), interval2.get(0));
        int end = Math.min(interval1.get(1), interval2.get(1));

        if (start > end) {
            return "NO";
        }

        int length = end - start + 1;

        if (isPrime(length)) {
            return "YES";
        } else {
            return "NO";
        }
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }

        return true;
    }
}
```

This code defines a class `Solution` with a method `intersection` that takes two intervals as input, calculates the intersection, and checks if its length is a prime number. The method `isPrime` is used to check if a number is prime.

The `intersection` method first calculates the start and end points of the intersection by taking the maximum of the start points and the minimum of the end points of the two intervals. If the start point is greater than the end point, it means the intervals do not intersect, so the method returns "NO".

Then, the method calculates the length of the intersection by subtracting the start point from the end point and adding 1. It then checks if the length is a prime number by calling the `isPrime` method. If it is, the method returns "YES", otherwise it returns "NO".