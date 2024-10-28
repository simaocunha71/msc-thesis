        // Create a set to store prime numbers
        Set<Integer> primeNumbers = new HashSet<>();

        // Add prime numbers less than 100 to the set
        for (int i = 2; i <= 100; i++) {
            if (isPrime(i)) {
                primeNumbers.add(i);
            }
        }

        // Check if the given number is the multiplication of 3 prime numbers
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

    // Helper function to check if a number is prime
    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
S:

This solution creates a set of prime numbers less than 100, then checks if the given number is the multiplication of 3 prime numbers from the set. It uses three nested loops to check all possible combinations of prime numbers. The `isPrime` helper function checks if a number is prime by testing divisibility from 2 to the square root of the number.

Here is the Java code for the solution:
```java
public boolean isMultiplyPrime(int a) {
    Set<Integer> primeNumbers = new HashSet<>();
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

private boolean isPrime(int num) {
    if (num <= 1) {
        return false;
   