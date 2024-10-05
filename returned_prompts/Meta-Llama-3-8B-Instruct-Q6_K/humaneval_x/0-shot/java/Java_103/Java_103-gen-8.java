```java
public Object roundedAvg(int n, int m) {
    if (n > m) {
        return -1;
    }
    int sum = 0;
    for (int i = n; i <= m; i++) {
        sum += i;
    }
    double avg = (double) sum / (m - n + 1);
    int roundedAvg = (int) Math.round(avg);
    String binary = Integer.toBinaryString(roundedAvg);
    return binary;
}
```
In this solution, we first check if `n` is greater than `m`, and if so, we return `-1` as per the problem statement.

Then, we calculate the sum of all integers from `n` to `m` (inclusive) using a `for` loop.

Next, we calculate the average of these integers by dividing the sum by the number of integers (`m - n + 1`).

We then round this average to the nearest integer using `Math.round()`.

Finally, we convert this rounded integer to binary using `Integer.toBinaryString()` and return the result as a string. If the rounded integer is `0`, the binary representation will be `"0"`. If the rounded integer is greater than `0`, the binary representation will be a string of `1`s. If the rounded integer is negative, the binary representation will be a string of `1`s followed by a `1` to indicate the negative sign. If the rounded integer is `1`, the binary representation will be `"1"`. If the rounded integer is `2`, the binary representation will be `"10"`. And so on.