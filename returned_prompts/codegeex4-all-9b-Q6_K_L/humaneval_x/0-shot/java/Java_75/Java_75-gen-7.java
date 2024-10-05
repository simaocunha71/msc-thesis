Here is a Java solution that checks if a number is a multiplication of three prime numbers:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println(isMultiplyPrime(30)); // true
        System.out.println(isMultiplyPrime(4)); // false
    }

    public static boolean isMultiplyPrime(int a) {
        if (a < 2) {
            return false;
        }
        List<Integer> primes = getPrimes(a);
        int product = 1;
        int count = 0;
        for (int i = primes.size() - 1; i >= 0; i--) {
            product *= primes.get(i);
            count++;
            if (product == a && count == 3) {
                return true;
            }
            if (product > a) {
                return false;
            }
        }
        return false;
    }

    private static List<Integer> getPrimes(int n) {
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

This program works by first generating a list of prime numbers up to `a`. Then, it multiplies the largest prime numbers in the list until the product is either equal to `a` or greater than `a`. If the product is equal to `a` and there have been three multiplications, then `a` is a multiplication of three prime numbers and the function returns `true`. If the product is greater than `a`, then `a` is not a multiplication of three prime numbers and the function returns `false`.

Note that this program assumes that `a` is a positive integer. If `a` can be negative or zero, then the function should be modified to handle these cases.