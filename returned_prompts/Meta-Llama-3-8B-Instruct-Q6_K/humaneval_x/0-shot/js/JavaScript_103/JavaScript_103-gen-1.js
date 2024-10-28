```
if (n > m) {
  return -1;
}

const sum = Array.from({ length: m - n + 1 }, (_, i) => n + i).reduce((a, b) => a + b, 0);

const avg = Math.round(sum / (m - n + 1));

return avg.toString(2);
```


Explanation:

1. First, we check if `n` is greater than `m`, and if so, we return -1 as per the problem statement.

2. Next, we calculate the sum of the integers from `n` to `m` using an array comprehension and the `reduce` method.

3. We then calculate the average by dividing the sum by the number of integers (`m - n + 1`).

4. We round the average to the nearest integer using the `Math.round` function.

5. Finally, we convert the rounded average to binary using the `toString(2)` method and return the result.

Note: This solution assumes that the input integers are non-negative. If negative integers are also allowed, additional checks and handling would be required.