```java
public boolean primeLength(String string) {
    int length = string.length();
    if (length <= 1) {
        return false;
    }
    for (int i = 2; i <= Math.sqrt(length); i++) {
        if (length % i == 0) {
            return false;
        }
    }
    return true;
}
```
Explanation:

*   We define a function `primeLength` that takes a string as an input and returns a boolean value.
*   We calculate the length of the input string and store it in the `length` variable.
*   We check if the length is less than or equal to 1, in which case we return `false` since prime numbers are greater than 1.
*   We then iterate from 2 to the square root of the length using a `for` loop.
*   For each iteration, we check if the length is divisible by the current number `i` using the modulo operator (`%`). If it is, we return `false` since the length is not a prime number.
*   If the loop completes without finding a divisor, we return `true` since the length is a prime number.

The examples provided in the problem statement are:
```java
primeLength("Hello") == true
primeLength("abcdcba") == true
primeLength("kittens") == true
primeLength("orange") == false
```
These examples demonstrate the correct behavior of the `primeLength` function. For example, the length of the string "Hello" is 5, which is a prime number, so the function returns `true`. Similarly, the length of the string "abcdcba" is 7, which is also a prime number, so the function returns `true`. On the other hand, the length of the string "orange" is 6, which is not a prime number, so the function returns `false`.