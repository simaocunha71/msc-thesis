Here is a Java solution for the problem:

```java
public int startsOneEnds(int n) {
    if(n == 1) {
        return 2;
    } else if(n == 2) {
        return 4;
    } else {
        return 18 * (int) Math.pow(10, n - 2);
    }
}
```
This function works by checking the length of the input integer `n`. If `n` is 1, it returns 2 (since the only one-digit numbers that start or end with 1 are 1 and 9). If `n` is 2, it returns 4 (since the only two-digit numbers that start or end with 1 are 10, 12, 11, 19). For all other values of `n`, it calculates the number of n-digit numbers that start or end with 1 by multiplying 18 by 10^(n-2). This works because for any n-digit number, there are 18 possible choices for the first digit (1, 2, ..., 9) and 10^(n-2) possible choices for the remaining digits.