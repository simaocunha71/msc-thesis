Here is a simple solution in Java. It uses a helper function to check if a number is prime and then checks the length of the string. 

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean primeLength(String string) {
        return isPrime(string.length());
    }

    private boolean isPrime(int number) {
        if (number <= 1) return false;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}
```
In the above code, the `isPrime()` function checks if a number is prime or not by iterating from 2 to the square root of the number and checking if the number is divisible by any number in this range. If it is, then it is not a prime number. If it is not divisible by any number in this range, then it is a prime number. 

The `primeLength()` function simply calls this helper function with the length of the input string. If the length of the string is a prime number, it returns true; otherwise, it returns false.