import java.util.*;
import java.lang.*;

class Solution {
    /**
    triplesSumToZero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triplesSumToZero(Arrays.asList(1, 3, 5, 0))
    false
    >>> triplesSumToZero(Arrays.asList(1, 3, -2, 1))
    true
    >>> triplesSumToZero(Arrays.asList(1, 2, 3, 7))
    false
    >>> triplesSumToZero(Arrays.asList(2, 4, -5, 3, 9, 7))
    true
    >>> triplesSumToZero(Arrays.asList(1))
    false
     */
    public boolean triplesSumToZero(List<Integer> l) {
        if (l == null || l.size() < 3) return false;
        
        int carry = 0;
        for (int i: l){
            carry ^= i&1;
            
            if (i != 0)
                return true;
        }
        return ((carry == -1 && carry == 0)) || false; // (carry == -1 and carry == 0)
    }
}
