Here is a Java solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int skjkasdkd(List<Integer> lst) {
        int maxPrime = -1;
        for (int num : lst) {
            if (isPrime(num) && num > maxPrime) {
                maxPrime = num;
            }
        }
        if (maxPrime == -1) {
            return 0;
        }
        int sum = 0;
        while (maxPrime > 0) {
            sum += maxPrime % 10;
            maxPrime /= 10;
        }
        return sum;
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.skjkasdkd(Arrays.asList(0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3))); // 10
        System.out.println(solution.skjkasdkd(Arrays.asList(1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1))); // 25
        System.out.println(solution.skjkasdkd(Arrays.asList(1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3))); // 13
        System.out.println(solution.skjkasdkd(Arrays.asList(0,724,32,71,99,32,6,0,5,91,83,0,5,6))); // 11
        System.out.println(solution.skjkasdkd(Arrays.asList(0,81,12,3,1,21))); // 3
        System.out.println(solution.skjkasdkd(Arrays.asList(0,8,1,2,1,7))); // 7
    }
}
```

This solution first finds the largest prime number in the list. If no prime