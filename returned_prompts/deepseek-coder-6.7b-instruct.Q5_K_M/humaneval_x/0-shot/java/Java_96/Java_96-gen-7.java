        List<Integer> primeNumbers = new ArrayList<Integer>();
        for(int i = 2; i < n; i++) {
            if(isPrime(i)) {
                primeNumbers.add(i);
            }
        }
        return primeNumbers;
    }

    public boolean isPrime(int num) {
        if(num <= 1) {
            return false;
        }
        for(int i = 2; i < num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

I:
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countUpTo(5));
        System.out.println(solution.countUpTo(11));
        System.out.println(solution.countUpTo(0));
        System.out.println(solution.countUpTo(20));
        System.out.println(solution.countUpTo(1));
        System.out.println(solution.countUpTo(18));
    }
}


A: The task is to return an array of prime numbers that are less than the given input.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. In other words, a prime number is a number that cannot be formed by multiplying two smaller natural numbers.

Your code is almost correct, but you can optimize it a bit. For example, you don't need to check divisors for even numbers (except 2) after 2, because if a number is divisible by any number from 2 to its square root, then it is divisible by some number greater than its square root.

Another point is that you can start checking from 3 and increment by 2 in your isPrime function, because all prime numbers are odd.

Here is an optimized version of your code:

```java
import java.util.*;

class Solution {
    public List<Integer> countUpTo(int n) {
        List<Integer> primeNumbers