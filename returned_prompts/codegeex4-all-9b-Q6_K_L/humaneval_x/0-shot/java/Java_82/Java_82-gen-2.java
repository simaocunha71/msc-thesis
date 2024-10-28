Here is a simple Java solution using the built-in `isPrime` method from the `MathUtils` class. 

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean primeLength(String string) {
        return isPrime(string.length());
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i = i + 6)
            if (n % i == 0 || n % (i + 2) == 0)
                return false;
        return true;
    }
}
```

The `isPrime` method checks if a number is prime or not. If the number is less than or equal to 1, it is not prime. If the number is less than or equal to 3, it is prime. If the number is divisible by 2 or 3, it is not prime. For numbers greater than 3 and not divisible by 2 or 3, it checks divisibility by all numbers up to its square root. If the number is divisible by any of these, it is not prime. If the number is not divisible by any of these, it is prime. 

The `primeLength` method checks the length of the string and returns the result of the `isPrime` method.