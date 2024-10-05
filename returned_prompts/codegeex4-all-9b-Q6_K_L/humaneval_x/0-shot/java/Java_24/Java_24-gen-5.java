```java
public int largestDivisor(int n) {
    int i = 1;
    while (i < n) {
        if (n % i == 0) {
            return i;
        }
        i++;
    }
    return n;
}
```
This function will iterate from 1 to n-1 and check if n is divisible by i. If it is, it will return i. If it doesn't find a divisor, it will return n.