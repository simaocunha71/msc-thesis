        return BigInteger.valueOf(2).pow(n).mod(BigInteger.valueOf(p)).intValue();
     }
}


A: import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Given a list of integers, return the integer that appears an odd number of times.
    There will always be only one integer that appears an odd number of times.
    >>> findOdd(Arrays.asList(1, 2, 3, 2, 1))
    3
    */
    public int findOdd(List<Integer> numbers) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int num : numbers) {
            counts.put(num, counts.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {
            if (entry.getValue() % 2 != 0) {
                return entry.getKey();
            }
        }
        return 0; // dummy return statement to satisfy compiler
    }
}

