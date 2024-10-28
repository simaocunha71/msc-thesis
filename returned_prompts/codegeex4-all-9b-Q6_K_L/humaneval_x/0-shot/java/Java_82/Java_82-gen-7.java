Here is a simple implementation of the `primeLength` function in Java. This function first checks if the length of the string is less than 2, in which case it returns false as prime numbers are greater than 1. Then it checks if the length is 2 or 3, in which case it returns true as 2 and 3 are prime numbers. For any other length, it checks if the length is divisible by any number from 2 to the square root of the length. If it is, it returns false; otherwise, it returns true.

```java
public boolean primeLength(String string) {
    int length = string.length();
    if (length < 2) {
        return false;
    }
    if (length == 2 || length == 3) {
        return true;
    }
    for (int i = 2; i * i <= length; i++) {
        if (length % i == 0) {
            return false;
        }
    }
    return true;
}
```

This function uses a common algorithm for checking if a number is prime, which is to check if it is divisible by any number from 2 to its square root. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked. If no factor is found, the number is prime.