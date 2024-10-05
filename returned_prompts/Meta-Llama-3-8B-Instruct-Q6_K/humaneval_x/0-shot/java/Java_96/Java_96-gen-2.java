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
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

Explanation:
The function `countUpTo(int n)` generates a list of prime numbers less than `n`. It does this by iterating over the numbers from 2 to `n-1` and checking if each number is prime using the `isPrime(int num)` helper function. If a number is prime, it is added to the result list. The `isPrime(int num)` function checks if a number is prime by checking if it has any divisors other than 1 and itself. If it finds a divisor, it returns `false`, indicating that the number is not prime. If it doesn't find any divisors, it returns `true`, indicating that the number is prime. The `Math.sqrt(num)` is used to optimize the primality check by only checking divisors up to the square root of the number. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.