        int result;
        if(n == 0)
            return 1;
        else
            result = power(2, n, p);

        return result;
    }

    public int power(int base, int exponent, int p) {
        int result = 1;
        while(exponent > 0) {
            if(exponent % 2 == 1) 
                result = (result * base) % p;
            exponent = exponent >> 1;
            base = (base * base) % p;
        }
        return result;
    }
}


A: You are correct. The method should calculate 2^n mod p. However, the method modp() should return 2^n mod p, not 3^n mod p. This is because 3^n mod p does not equal 2^n mod p for all n and p.

So, you should return 2 instead of 3 in the method modp().

And you should use the power function to calculate the power of a number modulo p. The power function should return the base raised to the power exponent modulo p.

Here is the corrected code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return 2^n modulo p  (be aware of numerics).
    >>> modp(3, 5)
    返回 3
    >>> modp(1101, 101)
    返回 2
    >>> modp(0, 101)
    返回 1
    >>> modp(3, 11)
    返回 8
    >>> modp(100, 101)
    返回 1
      */
    public int modp(int n, int p) {
        int result;
        if(n == 0)
            return 1;
        else
            result = power(2, n, p);
        return result;
    }

    public int power(int base, int exponent, int p) {
        int result = 1;
        while(exponent > 0) {
            if(exponent % 