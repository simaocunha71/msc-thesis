import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
     */
    public List<Integer> factorize(int n) {
        List<Integer> result = new ArrayList<>();
        int count = 1;

        for (int i = 2; ; i++) {
            if ((n % i == 0) && !(count > 1)) {
                result.add(i);
                n /= i;
                count++;
            } else break;
        }
        return result;
    }
}
