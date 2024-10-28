        if(n <= 1)
            return n;
        int fib = 1;
        int prevFib = 1;

        for(int i=2; i<n; i++) {
            int temp = fib;
            fib+= prevFib;
            prevFib = temp;
        }
        return fib;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.fib(10));
        System.out.println(sol.fib(1));
        System.out.println(sol.fib(8));
    }
}


A: The problem here is with your loop condition. It should be i<n, not i<=n. This is because you want to loop up to the n-th number in the sequence, not including the n-th number.

Here is the correct code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    */
    public int fib(int n) {
        if(n <= 1)
            return n;
        int fib = 1;
        int prevFib = 1;

        for(int i=2; i<n; i++) {
            int temp = fib;
            fib+= prevFib;
            prevFib = temp;
        }
        return fib;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.fib(10));
        System.out.println(sol.fib(1));
        System.out.println(sol.fib(8));
    }
}
```

This program will print the 10th, 1st and 8th Fibonacci numbers as 55, 1, and 21 respectively.

A