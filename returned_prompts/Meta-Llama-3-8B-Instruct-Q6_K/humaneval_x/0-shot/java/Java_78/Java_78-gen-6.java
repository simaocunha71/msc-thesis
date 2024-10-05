Here is a Java solution using a HashSet to store prime numbers and then counting the occurrences of these numbers in the input string.

```java
import java.util.*;

class Solution {
    public int hexKey(String num) {
        Set<Character> primeSet = new HashSet<>();
        for (char c = '2'; c <= 'F'; c++) {
            if (isPrime(Integer.parseInt(String.valueOf(c), 16))) {
                primeSet.add(c);
            }
        }
        int count = 0;
        for (char c : num.toCharArray()) {
            if (primeSet.contains(c)) {
                count++;
            }
        }
        return count;
    }

    private boolean isPrime(int n) {
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

This solution first creates a set of prime hexadecimal digits (2, 3, 5, 7, B, D) using a loop and the `isPrime` method. Then it iterates over the input string and counts the occurrences of prime digits in the set. The `isPrime` method checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers. If it is, the number is not prime and the method returns `false`. If the number is not divisible by any of these numbers, the method returns `true`. The `hexKey` method uses this set to count the occurrences of prime digits in the input string. The count is then returned.