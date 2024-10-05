    int count = 0;
    for (int i = 2; i <= a; i++) {
        if (a % i == 0) {
            count++;
            while (a % i == 0) {
                a /= i;
            }
        }
    }
    return count == 3;
}

public static void main(String[] args) {
    Solution sol = new Solution();
    System.out.println(sol.isMultiplyPrime(30)); // true
    System.out.println(sol.isMultiplyPrime(105)); // true
    System.out.println(sol.isMultiplyPrime(75)); // false
}
}


A: This problem can be solved by using a simple approach of prime factorization. 

Firstly, you need to determine whether the given number is a prime number or not. If it is a prime number, then the answer is false because it is not possible to express a single prime number as a multiplication of three different prime numbers. 

If the given number is not a prime, then you need to find out all the prime factors of that number and count the number of distinct prime factors. If the number of distinct prime factors is 3, then the given number can be expressed as a multiplication of three different prime numbers. 

Here is the Java code that solves the problem:

```java
import java.util.*;
class Solution{
    public boolean isMultiplyPrime(int n) {
        if (n <= 1)
            return false;
        if (n <= 3)
            return true;

        if (n % 2 == 0 || n % 3 == 0)
            return false;

        for (int i = 5; i * i <= n; i += 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;

        return true;
    }
    public static void main(String[] args){
        Solution sol = new Solution();
        System.out.println(sol.isMultiplyPrime(30)); // true
        System.out.println(sol.isMultiplyPrime(10