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

Explanation:
The function `countUpTo` takes an integer `n` as input and returns a list of prime numbers less than `n`. It does this by iterating from 2 to `n-1` and checking if each number is prime using the helper function `isPrime`. If a number is prime, it is added to the result list.

The `isPrime` function checks if a number `num` is prime by iterating from 2 to the square root of `num` and checking if `num` is divisible by any of these numbers. If `num` is divisible, it is not prime, so the function returns `false`. If `num` is not divisible by any of these numbers, it is prime, so the function returns `true`.

The time complexity of this solution is O(n*sqrt(n)), where n is the input integer. This is because the `isPrime` function iterates up to the square root of `num` for each number. The space complexity is O(n), where n is the number of prime numbers less than the input integer. This is because the result list can contain up to n prime numbers.