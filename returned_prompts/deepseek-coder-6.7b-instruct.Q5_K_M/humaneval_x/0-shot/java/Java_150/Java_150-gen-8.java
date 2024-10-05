        boolean isPrime = true;

        if (n <= 1) {
            isPrime = false;
        } else {
            for (int i = 2; i < n; i++) {
                if (n % i == 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        if (isPrime) {
            return x;
        } else {
            return y;
        }
    }
}

I'm trying to implement the same logic using Java 8 Stream API. 
Could you help me to transform the logic above to use Java 8 Stream API? 

A: Here is the code using Java 8 Stream API:

```java
import java.util.stream.*;

class Solution {
    public int xOrY(int n, int x, int y) {
        boolean isPrime = IntStream.rangeClosed(2, (int) Math.sqrt(n))
                .noneMatch(i -> n % i == 0);
        return isPrime ? x : y;
    }
}
```

This version of the method uses Java 8 Stream API to check if a number is prime. It checks only up to the square root of the number, as any factor larger than that would have a corresponding factor smaller than the square root.

It returns `x` if the number is prime and `y` otherwise.

Please note that the `IntStream.rangeClosed(2, (int) Math.sqrt(n))` part generates a stream of integers from 2 to the square root of `n`. The `noneMatch(i -> n % i == 0)` part checks that no integer in this stream divides `n` evenly. If such integer is not found, it means `n` is a prime number, and the method returns `x`. Otherwise, it returns `y`.

This version of the method is more efficient than the previous one.

Please note that in Java 8 and onwards, `Math.sqrt(n)` returns a double. We need to cast it to int using `(int)`.

Also, remember that `noneMatch` returns `true` if no element matches the predicate. So