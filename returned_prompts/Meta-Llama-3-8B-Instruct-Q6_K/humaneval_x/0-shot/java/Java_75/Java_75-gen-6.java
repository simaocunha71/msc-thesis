        Set<Integer> primeNumbers = new HashSet<Integer>();

        for (int i = 2; i <= 100; i++) {
            if (isPrime(i)) {
                primeNumbers.add(i);
            }
        }

        for (int i = 0; i < primeNumbers.size(); i++) {
            for (int j = i; j < primeNumbers.size(); j++) {
                for (int k = j; k < primeNumbers.size(); k++) {
                    if (a == primeNumbers.get(i) * primeNumbers.get(j) * primeNumbers.get(k)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
} // class Solution

C:
public boolean isMultiplyPrime(int a) {
    for (int i = 2; i <= 100; i++) {
        for (int j = i; j <= 100; j++) {
            for (int k = j; k <= 100; k++) {
                if (a == i * j * k && isPrime(i) && isPrime(j) && isPrime(k)) {
                    return true;
                }
            }
        }
    }
    return false;
}

private boolean isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
} // class Solution

C#:

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public bool IsMultiplyPrime(int a) {
        for (int i = 2; i <= 100; i++) {
            for (int j = i; j <= 100; j++) {
                for (int k = j; k <= 100; k++) {
                    if (a == i * j * k && IsPrime(i) && IsPrime(j) && IsPrime(k)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private bool IsPrime(int n