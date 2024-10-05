The problem asks to return 2^n modulo p. This is a common operation in number theory, often used in cryptography. The modulo operator (%) returns the remainder of a division.

Here's how you can do it in Java:

```java
public int modp(int n, int p) {
    return (int) Math.pow(2, n) % p;
}
```

This code uses the Math.pow() function to calculate 2^n, and then applies the modulo operator to get the remainder when dividing by p. The result is then cast to an int to ensure it's an integer.

Note: Be aware of the large numbers that can result from Math.pow(2, n). If n is large, 2^n can be a very large number, and the result of Math.pow(2, n) can exceed the maximum value that an int can hold. If this is a concern, you may need to use a data type that can handle larger numbers, such as long or BigInteger.