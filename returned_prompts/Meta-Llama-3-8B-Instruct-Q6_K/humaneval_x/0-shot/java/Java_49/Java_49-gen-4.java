Here is the Java solution for the problem:

```java
public int modp(int n, int p) {
    int result = 1;
    for(int i = 1; i <= n; i++) {
        result = (result * 2) % p;
    }
    return result;
}
```

Explanation:
The problem is to find 2^n modulo p. We can solve this using a simple loop. Initialize a variable `result` to 1. Then, for each iteration from 1 to `n`, multiply the `result` by 2 and take the modulo `p`. Finally, return the `result`.

For example, if `n = 3` and `p = 5`, the loop will run 3 times:

1. `result = 1 * 2 % 5 = 2`
2. `result = 2 * 2 % 5 = 4`
3. `result = 4 * 2 % 5 = 8`

So, the final result is `8`. If you call `modp(3, 5)`, it will return `8`. Similarly, you can test other inputs.