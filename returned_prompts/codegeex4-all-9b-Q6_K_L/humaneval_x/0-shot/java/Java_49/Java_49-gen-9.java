```java
public int modp(int n, int p) {
    if (p == 1) return 0;
    int result = 1;
    n = n % p;
    while (n > 0) {
        if ((n & 1) == 1) {
            result = (result * 2) % p;
        }
        n = n >> 1;
        p = (p * p) % p;
    }
    return result;
}
```
The above code is a Java implementation of the modp function. The function takes two integer inputs, n and p, and returns 2^n modulo p.

The function first checks if p is equal to 1. If so, it returns 0 as any number raised to the power of 0 is 0.

Next, the function initializes a variable result to 1. This variable will store the result of 2^n modulo p.

The function then takes the modulo of n with p and stores it back in n. This is done because we are only interested in the remainder when n is divided by p.

The function then enters a while loop that continues as long as n is greater than 0. Inside the loop, the function checks if the least significant bit of n is 1. If so, it multiplies result by 2 and takes the modulo with p. This is done because if the least significant bit of n is 1, then 2^n is odd, and we need to add 2^n to the result.

The function then right shifts n by 1 bit and squares p and takes the modulo with p. This is done because when we right shift n by 1 bit, we are essentially dividing n by 2, and when we square p and take the modulo with p, we are essentially multiplying p by itself and taking the modulo with p.

Once n becomes 0, the function returns the value of result, which is 2^n modulo p.

This function has a time complexity of O(log n) because it performs a loop that runs log n times.