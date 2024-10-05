        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                factors.add(i);
                n /= i;
            }
        }
        return factors;
    }
}

In the above code, we are iterating from 2 to n (both inclusive). For each number i, we are checking if it divides n. If it does, we add it to the factors list and divide n by i. We continue this process until n cannot be divided by i anymore. After this, we move to the next number i+1 and repeat the process. This way, we cover all possible factors of n. The result is a list of prime factors of n in ascending order.

Here is the Java code:

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
}
```

You can test it with the following code:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.factorize(8)); // [2, 2, 2]
        System.out.println(solution.factorize(25)); // [5, 5]
        System.out.println(solution.factorize(70)); // [2, 5, 7]
    }
}
```

This code will output:

```
[2, 2, 2]
[5, 5]
[2, 5, 7]
```

which are the prime factors of 8, 25, and 70 respectively.

The time complexity of this solution is O(n), and the space complexity is O(n) as we are storing the prime factors in a list.

This solution assumes