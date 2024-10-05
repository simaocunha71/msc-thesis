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
}

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.fib(10));
        System.out.println(s.fib(1));
        System.out.println(s.fib(8));
    }
}

This is a simple way to calculate the n-th Fibonacci number in Java. It uses an iterative approach where it calculates each Fibonacci number by adding the previous two numbers.

This solution has a time complexity of O(n) since we are looping through the range of numbers from 2 to n. The space complexity is O(1) since we only need a constant amount of space to store our variables.

This solution also handles the edge case of n=0 and n=1 correctly, returning n itself as the Fibonacci number.

If you want to calculate the n-th Fibonacci number recursively, you could use the following code:

```java
public int fib(int n) {
    if (n <= 1)
        return n;
    else
        return fib(n-1) + fib(n-2);
}
```

However, this solution has a time complexity of O(2^n) due to the recursive nature of the function. It's much slower than the iterative solution for large n.

Please let me know if you have any further questions about this code.
*/

import java.util.*;
import java.lang.*;

class Solution {
    public int fib(int n) {
        if(n <= 1)
            return n;
        int fib = 1;
        int prevFib = 1;

        for(int i=2; i<n; i++) {
            int temp =