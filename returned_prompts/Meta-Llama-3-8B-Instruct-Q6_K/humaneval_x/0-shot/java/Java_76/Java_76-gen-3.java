public class Solution {
    public boolean isSimplePower(int x, int n) {
        for (int i = 1; i <= x; i++) {
            double base = Math.pow(n, i);
            if ((int) base == x) {
                return true;
            }
        }
        return false;
    }
}

Explanation:
The function `isSimplePower` takes two integer parameters `x` and `n`. It checks if `x` is a simple power of `n`. A simple power of `n` means that `n` raised to some integer power `i` equals `x`.

The function iterates from `1` to `x` (inclusive) and checks if `n` raised to the power of `i` equals `x`. If it finds a match, it returns `true`. If it doesn't find a match after checking all powers up to `x`, it returns `false`.

Note that the `Math.pow` function returns a `double` value, so we need to cast the result to an `int` to compare it with `x`. This is safe because we're only checking powers up to `x`, so the result of `Math.pow` will always be an integer.

For example, if `x` is `8` and `n` is `2`, the function will iterate from `1` to `8` and check if `2` raised to the power of `i` equals `8`. It will find that `2` raised to the power of `3` equals `8`, so it will return `true`. If `x` is `3` and `n` is `2`, the function will iterate from `1` to `3` and check if `2` raised to the power of `i` equals `3`. It won't find a match, so it will return `false`.