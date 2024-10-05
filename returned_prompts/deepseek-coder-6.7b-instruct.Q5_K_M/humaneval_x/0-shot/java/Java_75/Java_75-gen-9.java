        int count = 0;
        boolean[] prime = new boolean[a+1];

        for(int i=0;i<=a;i++)
            prime[i] = true;

        for(int p = 2; p*p <=a; p++)
        {
            if(prime[p])
            {
                for(int i = p*p; i <= a; i += p)
                    prime[i] = false;
            }
        }

        for(int i = 2; i <= a; i++)
        {
            if(prime[i] && a % i==0)
            {
                count++;
                a /= i;
                i--;
            }
        }

        if (count > 2) return true;
        else return false;
    }
}

This code finds if the given number is the multiplication of 3 prime numbers.


A: You are correct. The problem statement is a bit confusing. If you want to check if a given number is a multiplication of 3 distinct prime numbers, you can modify your function as follows:

```java
public boolean isMultiplyPrime(int a) {
    int count = 0;
    List<Integer> primes = new ArrayList<>();

    for (int i = 2; i <= a; i++) {
        if (isPrime(i)) {
            primes.add(i);
        }
    }

    for (int prime : primes) {
        while (a % prime == 0) {
            a /= prime;
            count++;
        }
    }

    if (count == 3) {
        return true;
    } else {
        return false;
    }
}

private boolean isPrime(int num) {
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return num > 1;
}
```

This function first calculates all prime numbers up to the given number `a` using the `isPrime` function. Then it counts the number of times each prime