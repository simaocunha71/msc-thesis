Here is the solution for the problem:

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
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

In this solution, we first calculate the start and end points of the intersection interval. If the start is greater than the end, it means the intervals do not intersect, so we return "NO".

Then, we calculate the length of the intersection interval. We check if the length is a prime number using the `isPrime` function. If it is, we return "YES", otherwise, we return "NO". The `isPrime` function checks if a number is prime by checking if it has any divisors other than 1 and itself. If it does, it returns `false`, otherwise, it returns `true`. The time complexity of this solution is O(1) and the space complexity is O(1). 