import java.util.*;

class Solution {
    public int solve(List<Integer> lst) {
        int max = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (isPrime(lst.get(i))) {
                max = lst.get(i);
            }
        }
        return sum(max);
    }

    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static int sum(int num) {
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        return sum;
    }
}

