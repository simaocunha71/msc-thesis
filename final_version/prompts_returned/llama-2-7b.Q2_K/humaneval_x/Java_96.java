import java.util.*;
import java.lang.*;

class Solution {
    /**
    Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    countUpTo(5) => [2,3]
    countUpTo(11) => [2,3,5,7]
    countUpTo(0) => []
    countUpTo(20) => [2,3,5,7,11,13,17,19]
    countUpTo(1) => []
    countUpTo(18) => [2,3,5,7,11,13,17]
     */
    public List<Integer> countUpTo(int n) {
        if (n == 0 || n < 0) return Collections.emptyList();
        Deque<Integer> deque = new ArrayDeque<>();
        
        while (!deque.isEmpty() && !deque.peekFirst().equals(n)) {
            int cur = deque.pop();
            if (cur != 0 && isPrime(cur) == false) {
                if (cur % n == 0) return Collections.emptyList();
            } else if (cur == 0) {
                continue;
            }
            List<Integer> ret = new ArrayList<>();
            for (int i : deque) {
                if (!(i >= 1 && i <= n)) continue;
                ret.add(i);
            }
            return Collections.unmodifiableList(ret);
        }
        
        return Collections.emptyList();
    }
    
    private boolean isPrime(int prime) {
       if (prime == 0 || prime % 2 == 0 || prime % 3 == 0 || 
              prime % 5 == 0 || prime % 7 == 0 || 
              prime % 11 == 0 || prime % 13 == 0) {
            return true;
       } else if (prime < 99 && this.getAllFactors(prime, false) != null && getAllFactors(prime,