        if (n <= 0) {
            return -1;
        }

        ArrayList<Integer> primes = new ArrayList<>();
        ArrayList<Integer> fibs = new ArrayList<>();

        primes.add(2);
        fibs.add(1);
        fibs.add(1);

        int i = 3;
        while (primes.size() < n || fibs.size() < n) {
            if (isPrime(i) && !primes.contains(i)) {
                primes.add(i);
            }
            int fib = fibs.get(fibs.size() - 1) + fibs.get(fibs.size() - 2);
            if (fib <= 46368) {
                fibs.add(fib);
            } else {
                break;
            }
            i += 2;
        }

        return primes.get(n - 1);
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n <= 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}

```


## Explanation
This program first checks if the input is less than or equal to 0. If it is, it returns -1 because there are no Fibonacci prime numbers less than or equal to 0. 

Then it initializes two lists, `primes` and `fibs`, to store prime numbers and Fibonacci numbers respectively.

It adds 2 to the `primes` list and 1 to the `fibs` list because 2 is the smallest prime number and 1 is the first Fibonacci number.

It then enters a loop that continues until the `