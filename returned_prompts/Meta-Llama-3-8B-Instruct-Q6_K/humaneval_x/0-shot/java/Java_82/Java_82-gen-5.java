Here is a Java function that checks if the length of a given string is a prime number:

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

This function first calculates the length of the input string. Then it checks if the length is less than or equal to 1, in which case it returns false because prime numbers are greater than 1. 

Next, it iterates from 2 to the square root of the length, and for each number, it checks if the length is divisible by that number. If it is, the function returns false because the length is not a prime number. 

If the function has not returned false by the end of the loop, it returns true because the length is likely to be a prime number. 

Note that this function uses the fact that a composite number must have a factor less than or equal to its square root. Therefore, if a number has no factors less than or equal to its square root, it is likely to be a prime number. 

This function should work correctly for strings of any length, not just those with prime lengths. 

Also, note that this function is case-sensitive and considers spaces and punctuation as part of the string length. If you want to ignore these, you can remove them from the string before calculating its length. 