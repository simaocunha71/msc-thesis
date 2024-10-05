        int largestDivisor = 1;
        for(int i=2; i<=n/2; i++){
            if(n % i == 0){
                largestDivisor = i;
            }
        }
        return largestDivisor;
    }
}

This solution checks from 2 to n/2 to see if it is divisible evenly (i.e., the remainder when divided is zero). If it is, that is the largest divisor. It starts at 2 because every number is divisible by 1, and it stops at n/2 because no number can have a larger divisor than itself.

This is a basic solution and can be optimized. For example, you can check up to the square root of n because a larger factor of n must be a multiple of a smaller factor that has already been checked.

```java
public int largestDivisor(int n) {
    int largestDivisor = 1;
    for(int i=2; i*i<=n; i++){
        if(n % i == 0){
            if(i*i != n)
                largestDivisor = i;
            else
                largestDivisor = n/i;
        }
    }
    return largestDivisor;
}
```
In this optimized solution, we check up to sqrt(n) instead of n/2. If n is a perfect square, we only need to check the square root once, otherwise we check up to n/2. For non-squares, we also update the largest divisor if n is divided by i.
 */

// 15 / 2 = 7, 15 / 3 = 5, 15 / 4 = 3, 15 / 5 = 3, 15 / 6 = 3, 15 / 7 = 2
// 15 / 8 = 1, 15 / 9 = 1, 15 / 10 = 1, 15 / 11 = 1, 15 / 12 = 1, 15 / 13 = 1, 15 / 14 = 1, 15 / 15 = 1
// Largest divisor is 5

// 20 / 2 = 