        List<Integer> primeNumbers = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                primeNumbers.add(i);
            }
        }
        return primeNumbers;
    }

    private boolean isPrime(int num) {
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
}

This is a Java solution for the problem. The isPrime function checks if a given number is prime. The countUpTo function iterates from 2 to n-1 and adds the prime numbers to a list. The list is then returned.

Note: This solution has a time complexity of O(n^2), because of the isPrime function which has a time complexity of O(n). If you want to optimize it, you can use the Sieve of Eratosthenes algorithm which has a time complexity of O(n log log n).
Also, the problem statement asks for primes less than n, not up to n. So, the for loop should iterate from 2 to n, not n-1.

Here is the Sieve of Eratosthenes algorithm:

```java
public List<Integer> countUpTo(int n) {
    boolean[] isPrime = new boolean[n];
    Arrays.fill(isPrime, true);
    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j < n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    List<Integer> primeNumbers = new ArrayList<>();
    for (int i = 2; i < n; i++) {
        if (isPrime[i]) {
            primeNumbers.add(i);
        }
    }
    return primeNumbers;
}
```

This version of the function uses a boolean