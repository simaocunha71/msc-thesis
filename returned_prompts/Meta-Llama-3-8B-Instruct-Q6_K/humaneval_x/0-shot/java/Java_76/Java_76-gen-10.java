Here is a Java function that implements the `isSimplePower` method:

```java
public boolean isSimplePower(int x, int n) {
    for (int i = 1; Math.pow(n, i) <= x; i++) {
        if (Math.pow(n, i) == x) {
            return true;
        }
    }
    return false;
}
```

This function iterates over all possible powers of `n` and checks if the power is equal to `x`. If it finds a match, it returns `true`. If it doesn't find a match after checking all possible powers, it returns `false`.

Here's a breakdown of how the function works:

1. The function starts a loop from `i = 1` and keeps incrementing `i` until `n` raised to the power of `i` is greater than `x`.
2. Inside the loop, the function checks if `n` raised to the power of `i` is equal to `x`. If it is, the function returns `true`.
3. If the loop completes without finding a match, the function returns `false`.

This function has a time complexity of O(log(x)), where `x` is the input number, because the loop iterates over the powers of `n` until it reaches `x`. The space complexity is O(1), which means the function uses a constant amount of space, because it only uses a few variables to store the loop counter and the power of `n`.