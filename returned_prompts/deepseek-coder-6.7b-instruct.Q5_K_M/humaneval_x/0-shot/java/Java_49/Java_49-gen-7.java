        if (n == 0) return 1;
        if (n == 1) return 2;

        long result = 1;
        long base = 2;
        long mod = p;

        while (n > 0) {
            if ((n & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            n >>= 1;
        }

        return (int) result;
    }
}

This solution uses bitwise operations to reduce the time complexity of calculating 2^n. If n is even, then it is transformed into n/2. If n is odd, then it is transformed into (n-1)/2. In this way, the time complexity of the algorithm is reduced to O(logn).

For example, let's take modp(3, 5) as an example.

- n = 3, p = 5
- (n & 1) == 1, so base = (base * base) % p = 4, n = 2
- (n & 1) == 0, so skip this step, n = 1
- (n & 1) == 1, so result = (result * base) % p = 4 * 2 % 5 = 0, n = 0

So, the result is 0.

This solution works for all positive integers n and p.
*/

// This is a Java solution for the problem

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.modp(3, 5)); // 3
        System.out.println(solution.modp(1101, 101)); // 2
        System.out.println(solution.modp(0, 101)); // 1
        System.out.println(solution.modp(3, 11)); // 8
        System.out.println(solution.modp(100, 101)); // 1
    }
}
```

This Java program will output:

```
3
2
1
8