Here is a Java solution for the problem. This solution uses a helper function to check if a number is prime and then iterates from 2 to n-1 to find all prime numbers less than n.

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    public boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

This solution has a time complexity of O(n*sqrt(n)) because of the isPrime function, which iterates up to the square root of the number to check for divisibility. The space complexity is O(n) because of the list of prime numbers. This solution is not efficient for large values of n, but it is simple and easy to understand. For a more efficient solution, you could use a sieve algorithm to generate all prime numbers up to n.