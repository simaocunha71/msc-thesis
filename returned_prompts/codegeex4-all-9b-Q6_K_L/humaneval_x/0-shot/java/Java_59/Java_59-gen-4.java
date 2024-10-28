```java
public int largestPrimeFactor(int n) {
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                n /= i;
            }
        }
        return n;
    }
```
The code above is a brute force solution to find the largest prime factor of n. It starts from 2 and checks each number if it is a factor of n. If it is, it divides n by that factor and continues to the next number. Finally, it returns n, which is the largest prime factor of the original n.