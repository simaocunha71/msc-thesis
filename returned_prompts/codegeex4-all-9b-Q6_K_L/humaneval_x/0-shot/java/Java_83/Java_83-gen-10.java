Here is the Java code that solves the problem:

```java
public int startsOneEnds(int n) {
    if (n == 1) {
        return 2;
    }
    int total = 9 * (int) Math.pow(10, n - 2);
    total += 2 * (int) Math.pow(10, n - 1);
    return total;
}
```
The method `startsOneEnds(int n)` takes a positive integer `n` as input and returns the count of the numbers of `n`-digit positive integers that start or end with 1.

Here's the explanation of the code:

1. If `n` is equal to 1, the method returns 2. This is because the only 1-digit positive integers that start or end with 1 are 1 and 0.
2. If `n` is greater than 1, the method calculates the total count of `n`-digit positive integers that start or end with 1.
3. The count of `n`-digit positive integers that start with 1 is `(9 * 10^(n-2))`. This is because the first digit can be any digit except 0, and the remaining `n-1` digits can be any digit from 0 to 9.
4. The count of `n`-digit positive integers that end with 1 is `2 * 10^(n-1)`. This is because the first `n-1` digits can be any digit from 0 to 9, and the last digit must be 1.
5. The method adds the counts of `n`-digit positive integers that start or end with 1 and returns the total.

Note: This code assumes that `n` is a positive integer greater than 0. If `n` is less than or equal to 0, the method will return incorrect results.