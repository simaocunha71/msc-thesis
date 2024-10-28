Here is a simple way to solve this problem in Java:

```java
public int largestDivisor(int n) {
    for (int i = n / 2; i >= 1; i--) {
        if (n % i == 0) {
            return i;
        }
    }
    return -1; // return -1 if no divisor is found
}
```

This program starts from half of the given number and goes down to 1, checking if each number divides the given number evenly. If it finds a number that divides the given number evenly, it returns that number. If it doesn't find any number that divides the given number evenly, it returns -1.