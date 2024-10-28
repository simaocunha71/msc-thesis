To solve this problem, we need to check if the given number can be expressed as a multiplication of three distinct prime numbers. Here's a possible solution in Java:

```java
import java.util.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        if (a <= 1) {
            return false;
        }
        
        List<Integer> primes = generatePrimes(a);
        
        for (int i = 0; i < primes.size(); i++) {
            for (int j = i + 1; j < primes.size(); j++) {
                for (int k = j + 1; k < primes.size(); k++) {
                    if (primes.get(i) * primes.get(j) * primes.get(k) == a) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    private List<Integer> generatePrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        
        return primes;
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
```

In this solution, we first generate a list of prime numbers up to the given number `a`. Then, we use three nested loops to check if any three distinct prime numbers can multiply to give `a`. If we find such a combination, we return `true`. Otherwise, we return `false`.

Note that the `isPrime` method is used to check if a number is prime. It iterates from 2 to the square root of the number and checks if it is divisible by any number in that range. If it is divisible by any number, it is not prime. Otherwise, it is prime.