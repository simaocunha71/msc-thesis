        if (n < 0)
            throw new IllegalArgumentException("n must be greater or equal to 0");

        if (n == 0 || n == 1)
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

This solution uses a dynamic programming approach to compute the nth term in the fibfib sequence. It stores the computed values in an array 'fib' which is indexed by the term number. The time complexity of this solution is O(n) and the space complexity is also O(n).

The dynamic programming approach is used to avoid the redundant computation of terms in the sequence that are already computed. This makes the solution much more efficient than a recursive approach, which would have a time complexity of O(3^n).

The solution also handles the base cases (n = 0, n = 1, and n = 2) directly and does not require any special handling for these cases.

The solution throws an IllegalArgumentException if n is negative, as per the problem statement.

The solution assumes that n will be a non-negative integer. If n can be a negative number, the solution should be modified to handle this case.

This solution is written in Java and should be compatible with any Java environment.

Please note that the time complexity and space complexity are worst-case scenarios. In practice, the time complexity can be significantly improved by using a constant amount of space.

This solution is correct and efficient for all non-negative integer inputs. However, it may have issues with large inputs due to the limitation of Java's int data type.

Please test this solution with your own data to ensure it meets your requirements.
