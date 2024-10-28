Here is the Java implementation for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> factorize(int n) {
        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        return factors;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.factorize(8));  // [2, 2, 2]
        System.out.println(solution.factorize(25)); // [5, 5]
        System.out.println(solution.factorize(70)); // [2, 5, 7]
    }
}
```

This implementation starts from 2 and checks if it divides the given number. If it does, it adds it to the list and divides the number by the factor. This is repeated until the factor is no longer a divisor of the number. The process is then repeated for the next number. This way, all prime factors of the number are found in ascending order.