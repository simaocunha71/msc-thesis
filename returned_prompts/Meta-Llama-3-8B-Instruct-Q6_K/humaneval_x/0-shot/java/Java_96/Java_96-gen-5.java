Here is a Java solution that uses a helper function to check if a number is prime and then generates the list of prime numbers:

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
    }

    private boolean isPrime(int num) {
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

This solution works by iterating over all numbers from 2 to n-1 and checking if each number is prime using the helper function `isPrime`. If the number is prime, it is added to the result list. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it is not prime. If it is not divisible by any of these values, it is prime. The function returns true if the number is prime and false otherwise. This solution has a time complexity of O(n sqrt(n)) because it checks each number up to n and for each number, it checks up to its square root. This solution can be optimized by using a more efficient primality test, such as the Sieve of Eratosthenes algorithm. 