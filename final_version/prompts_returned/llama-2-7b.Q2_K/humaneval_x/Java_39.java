import java.util.*;
import java.lang.*;

class Solution {
    /**
    primeFib returns n-th number that is a Fibonacci number and it's also prime.
    >>> primeFib(1)
    2
    >>> primeFib(2)
    3
    >>> primeFib(3)
    5
    >>> primeFib(4)
    13
    >>> primeFib(5)
    89
     */
    public int primeFib(int n) {
        if (n <= 0 || n == 2 || n == 3 ) return "You're a liar!"; // return the number that I'm not allowed to use!
        else {
            HashMap<Integer, Integer> hash = new HashMap();
            for(int i=1; i<=n-1; ++i) {
                if(hash.containsKey(i)) continue;
                int fibonacciFactorials = 0;
                for (int j : FibonacciSequence) {
                    if((j%i == 0 && j % n != 0 ) || (j%n != 0 && j%i == 0)) {
                        hash.put(j, fibonacciFactorials);
                        break;
                    }
                }
            }
            return -1;// I'm a liar!
        }
    }
}
