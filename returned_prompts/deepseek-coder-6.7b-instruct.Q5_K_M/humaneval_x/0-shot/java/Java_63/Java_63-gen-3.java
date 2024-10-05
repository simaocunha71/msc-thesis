        if (n < 0) {
            throw new IllegalArgumentException("n should be >= 0");
        }
        if (n == 0 || n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;
        for (int i = 3; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }
        return fib[n];
    }
}

Explanation:
The main idea of the solution is to create an array fib of size n+1 and store the FibFib number at each index. fib[0] is initialized as 0, fib[1] is initialized as 0, and fib[2] is initialized as 1. For each i in the range from 3 to n, the i-th FibFib number is computed as the sum of the (i-1)-th, (i-2)-th, and (i-3)-th FibFib numbers. Finally, the n-th FibFib number is returned.

The time complexity of this solution is O(n), and the space complexity is O(n).

The function will throw an IllegalArgumentException if n is negative. This is because the FibFib sequence is not defined for negative indices.
*/

// test the function
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fibfib(1)); // 0
        System.out.println(sol.fibfib(5)); // 4
        System.out.println(sol.fibfib(8)); // 24
    }
}

// this will print:
// 0
// 4
// 24
```

## Tests

Here are some test cases you can use to validate your solution:

```java
assert fibfib(0) == 0;
assert fib