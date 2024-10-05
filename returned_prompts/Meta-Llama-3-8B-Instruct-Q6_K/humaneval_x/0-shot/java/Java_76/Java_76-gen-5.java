Here is a simple and efficient solution in Java:

```java
public boolean isSimplePower(int x, int n) {
    for (int i = 1; i <= x; i++) {
        if (Math.pow(n, i) == x) {
            return true;
        }
    }
    return false;
}
```

This function iterates through all possible powers of `n` and checks if any of them is equal to `x`. If it finds a match, it returns `true`. If it doesn't find a match after checking all powers, it returns `false`.

Please note that this function may not be efficient for large values of `x` or `n` because it uses floating point arithmetic and may incur precision errors. For a more robust solution, you could consider using logarithms or other mathematical techniques.

Here is a more efficient solution using logarithms:

```java
public boolean isSimplePower(int x, int n) {
    if (x < 1 || n < 1) {
        return false;
    }
    double logX = Math.log(x) / Math.log(n);
    return Math.floor(logX) == logX;
}
```

This function first checks if `x` and `n` are less than 1, in which case it returns `false`. Then it calculates the logarithm of `x` to the base `n` and checks if the result is an integer. If it is, then `x` is a simple power of `n` and the function returns `true`. Otherwise, it returns `false`. This solution is more efficient and robust than the previous one, but it still has some limitations due to the use of floating point arithmetic. For a more robust solution, you could consider using logarithmic tables or other mathematical techniques.