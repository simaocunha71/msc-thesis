public boolean isSimplePower(int x, int n) {
    for (int i = 1; ; i++) {
        long pow = (long) Math.pow(n, i);
        if (pow == x) {
            return true;
        }
        if (pow > x) {
            return false;
        }
    }
}
Explanation:
The function `isSimplePower` takes two integer parameters `x` and `n`. It checks whether `x` is a simple power of `n` or not.

The function iterates over the powers of `n` using a for loop, starting from `i = 1`. For each `i`, it calculates the `i-th` power of `n` using the `Math.pow` method, which returns a `double` value.

The function checks if the calculated power is equal to `x`. If it is, the function returns `true`, indicating that `x` is a simple power of `n`.

If the calculated power is greater than `x`, the function returns `false`, indicating that `x` is not a simple power of `n`.

Note that the loop continues indefinitely, but the function will return `true` or `false` as soon as it finds a match or determines that `x` is not a simple power of `n`. This is because the powers of `n` will eventually exceed `x` if `x` is not a simple power of `n`.

The use of a `long` variable `pow` is necessary to avoid overflow when calculating the powers of `n`. The `Math.pow` method returns a `double` value, and the result of the power operation may exceed the range of an `int` variable. By using a `long` variable, we can store the result of the power operation without losing precision. However, if the result of the power operation exceeds the range of a `long` variable, the function will still return `false`. This is because the `long` data type has a larger range than the `int` data type, but it is still limited. If the result of the power operation exceeds the range of a `long` variable, it will exceed the range of an `int` variable as well, and the function will correctly return `false`.