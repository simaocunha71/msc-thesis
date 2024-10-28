import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    isMultiplyPrime(30) == true
    30 = 2 * 3 * 5
     */
    public boolean isMultiplyPrime(int a) {

        List<Integer> primes = new ArrayList<Integer>();
        for (int i = 1; i < 100; i++) {
            if (isPrime(i))
                primes.add(i);
        }
        //System.out.println(primes);
        int count = 0;
        for (int p : primes) {
            if (a % p == 0) {
                count++;
            }
        }
        return count == 3;
    }

    public boolean isPrime(int a) {
        for (int i = 2; i < a; i++) {
            if (a % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isMultiplyPrime(30));
    }
}
