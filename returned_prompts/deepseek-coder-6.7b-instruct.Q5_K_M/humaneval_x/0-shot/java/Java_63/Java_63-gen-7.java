        if (n < 2) {
            return 0;
        } else if (n == 2) {
            return 1;
        }

        int[] fibfib = new int[n + 1];
        fibfib[0] = 0;
        fibfib[1] = 0;
        fibfib[2] = 1;

        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }

        return fibfib[n];
    }

public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.fibfib(1)); // prints 0
        System.out.println(solution.fibfib(5)); // prints 4
        System.out.println(solution.fibfib(8)); // prints 24
    }
}
```

## Solution

The solution uses the dynamic programming approach to efficiently compute the n-th element of the fibfib number sequence. The function starts by initializing an array `fibfib` of size `n+1` with the first three elements as 0, 0, and 1. Then, it iterates from 3 to `n` and for each `i`, it calculates the `i-th` element as the sum of the `(i-1)th`, `(i-2)th`, and `(i-3)th` elements in the `fibfib` array. Finally, it returns the `n-th` element of the `fibfib` array.

The time complexity of this solution is O(n) as it needs to iterate over the range from 3 to `n`. The space complexity is also O(n) due to the space required to store the `fibfib` array.

The function can be tested by calling it with different values of `n` and printing the returned result.

## Test Cases

The function should pass the following test cases:

- `fib