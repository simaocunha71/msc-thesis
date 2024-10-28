import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> primeList = new ArrayList<>();
        if (n <= 1) {
            return primeList;
        }
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primeList.add(i);
            }
        }
        return primeList;
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}