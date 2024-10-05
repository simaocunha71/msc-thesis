        if (n < 2)
            return 0;
        if (n == 2)
            return 1;

        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;

        for(int i = 3; i <= n; i++){
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }

        return fib[n];
    }
}


A: Here's a more optimal solution using dynamic programming. This solution uses an array to store the fibfib sequence up to the nth number. This approach reduces the time complexity of the solution to O(n).

```java
public class Solution {
    public int fibfib(int n) {
        if (n < 2)
            return 0;
        if (n == 2)
            return 1;

        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 0;
        fib[2] = 1;

        for(int i = 3; i <= n; i++){
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
        }

        return fib[n];
    }
}
```
In this solution, the base cases are defined for n = 0 and n = 1 (both return 0) and n = 2 (return 1). Then, an array is created to store the fibfib sequence up to the nth number. The loop goes from 3 to n and calculates the fibfib number at each position using the formula given in the problem description. Finally, the nth fibfib number is returned from the array.

This solution is efficient because it avoids the repeated calculations of the same fibfib numbers, which would be the case with a naive recursive solution. It also uses memory to store previously calculated fibfib numbers, which can be a significant time saver for large inputs.

The time complexity of this solution is O(n), and the space complexity is O(n), where n is the input