        int sum = 0;
        for(int i = 2; i <= n; i += 2){
            sum += i;
            if(sum == n)
                return true;
        }
        return false;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.isEqualToSumEven(4));
        System.out.println(solution.isEqualToSumEven(6));
        System.out.println(solution.isEqualToSumEven(8));
    }
}


A: You have to keep in mind that the sum of the first N even numbers is equal to N*(N+1). So, to sum N*4 even numbers, you need to sum 4*N*(N+1)/2 even numbers.

In your code, you are checking whether the sum of the first N even numbers equals to n. But you have to check whether the sum of the first N*(N+1)/2 even numbers equals to n. 

Let me correct the code:


```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    isEqualToSumEven(4) == false
    isEqualToSumEven(6) == false
    isEqualToSumEven(8) == true
      */
    public boolean isEqualToSumEven(int n) {
        if (n % 2 != 0 || n < 8)
            return false;

        for (int i = 2; i <= n / 2; i += 2) {
            int sum = i * (i + 1) / 2 * 4;
            if (sum == n)
                return true;
        }
        return false;
    }

    public static void main(String[] args) throws java.lang.Exception {
        Solution solution = new Solution();
        System.out.println(solution.isEqualToSumEven(4));
        System.out.println(solution.isEqualToSumEven(6