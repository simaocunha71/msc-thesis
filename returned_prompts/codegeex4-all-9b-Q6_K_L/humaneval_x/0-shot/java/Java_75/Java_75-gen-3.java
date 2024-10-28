Here is a Java solution for the problem. The function isMultiplyPrime checks if the given number is the multiplication of 3 prime numbers. It uses the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to the given number.

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isMultiplyPrime(int a) {
        List<Integer> primes = sieveOfEratosthenes(a);
        if (primes.size() < 3) {
            return false;
        }
        for (int i = 0; i < primes.size() - 2; i++) {
            for (int j = i + 1; j < primes.size() - 1; j++) {
                for (int k = j + 1; k < primes.size(); k++) {
                    if (primes.get(i) * primes.get(j) * primes.get(k) == a) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private List<Integer> sieveOfEratosthenes(int n) {
        boolean prime[] = new boolean[n+1];
        for(int i=0;i<=n;i++)
            prime[i] = true;
 
        for(int p = 2; p*p <=n; p++)
        {
            if(prime[p])
            {
                for(int i = p*p; i <= n; i += p)
                    prime[i] = false;
            }
        }
        List<Integer> primeNumbers = new ArrayList<>();
        for(int i = 2; i <= n; i++)
            if(prime[i])
                primeNumbers.add(i);
        return primeNumbers;
    }
}
```

This solution has a time complexity of O(n^3) due to the three nested loops. The space complexity is O(n) because we store all the prime numbers up to n in a list. If the input number is large, this solution may not be efficient. In that case, you may need to use a more efficient algorithm.