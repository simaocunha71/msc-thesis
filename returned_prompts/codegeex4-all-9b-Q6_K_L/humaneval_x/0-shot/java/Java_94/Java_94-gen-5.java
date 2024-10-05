import java.util.*;
import java.lang.*;

class Solution {
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = Integer.MIN_VALUE;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        if (maxPrime == Integer.MIN_VALUE) {
            return 0;
        }
        int sum = 0;
        while (maxPrime != 0) {
            sum += maxPrime % 10;
            maxPrime /= 10;
        }
        return sum;
    }
}