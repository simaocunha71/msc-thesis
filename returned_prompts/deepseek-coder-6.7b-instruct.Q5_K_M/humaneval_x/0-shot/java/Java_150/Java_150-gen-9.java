        if (isPrime(n))
            return x;
        else
            return y;
    }

    public boolean isPrime(int num) {
        if (num <= 1)
            return false;
        for (int i = 2; i < num; i++)
            if (num % i == 0)
                return false;
        return true;
    }
}

*/


import java.util.*;
import java.lang.*;

class Solution  {
    public int xOrY(int n, int x, int y)  {
        if (isPrime(n))
            return x;
        else
            return y;
    }

    public boolean isPrime(int num) {
        if (num <= 1)
            return false;
        for (int i = 2; i < num; i++)
            if (num % i == 0)
                return false;
        return true;
    }
}

//Test Solution 
public class Test {
    public static void main (String[] args) throws java.lang.Exception {
        Solution sol = new Solution();
        System.out.println(sol.xOrY(7, 34, 12)); // 34
        System.out.println(sol.xOrY(15, 8, 5)); // 5
    }
}

//Explanation:
//In the first test case, 7 is a prime number, so the method returns x which is 34.
//In the second test case, 15 is not a prime number, so the method returns y which is 5.
//The isPrime() method checks if a number is a prime number or not. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself. The isPrime() method checks if a number is divisible by any number from 2 to num-1. If it is, then num is not a prime number and the method returns false. Otherwise, it returns true.
//If the number is a prime number, then the method xOrY() returns x. If not, it returns y.

//Time complexity: The time