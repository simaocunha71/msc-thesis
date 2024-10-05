Here is the Java implementation of the function `isSimplePower`:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isSimplePower(int x, int n) {
        // Check if x is a power of n
        return Math.pow(n, Math.round(Math.log(x) / Math.log(n))) == x;
    }
}
```

In this function, we use the properties of logarithms to check if `x` is a power of `n`. The `Math.log(x) / Math.log(n)` expression gives us the exponent to which `n` should be raised to get `x`. We round this value to the nearest integer using `Math.round()`. Then, we raise `n` to this exponent using `Math.pow()` and check if the result is equal to `x`. If it is, then `x` is a power of `n`, and the function returns `true`. Otherwise, it returns `false`.