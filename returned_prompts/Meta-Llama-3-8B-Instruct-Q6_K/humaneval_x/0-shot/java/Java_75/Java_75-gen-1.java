        // Initialize a boolean array, prime, of size 100, and set all elements to true. 
        // A value in prime[i] will finally be false if i is not a prime, else true.
        boolean[] prime = new boolean[100];
        for (int p = 2; p * p <= 100; p++) {
            // Update all multiples of p
            for (int i = p * p; i <= 100; i += p) {
                prime[i] = false;
            }
        }

        // Check if the given number is a multiplication of 3 prime numbers
        for (int i = 2; i <= 100; i++) {
            if (prime[i]) {
                for (int j = i; j <= 100; j++) {
                    if (prime[j]) {
                        for (int k = j; k <= 100; k++) {
                            if (prime[k]) {
                                if (a == i * j * k) {
 return true;
                                }
                            }
                        }
                    }
                }
            }
        }

        return false;
    }
}
}
S:
The problem is asking to write a function that checks if a given number is the product of three prime numbers. 

Here is the solution:

```java
public boolean isMultiplyPrime(int a) {
    // Initialize a boolean array, prime, of size 100, and set all elements to true. 
    // A value in prime[i] will finally be false if i is not a prime, else true.
    boolean[] prime = new boolean[100];
    for (int p = 2; p * p <= 100; p++) {
        // Update all multiples of p
        for (int i = p * p; i <= 100; i += p) {
            prime[i] = false;
        }
    }

    // Check if the given number is a multiplication of 3 prime numbers
    for (int i = 2; i <= 100; i++) {
        if (prime[i]) {
            for (int j = i; j <= 100; j++) {
                if (prime[j]) {
                    for (int k = j; k <= 100; k++) {
                        if (prime[k]) {
                            if (a == i * j * k) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
    }

    return false;
}
``