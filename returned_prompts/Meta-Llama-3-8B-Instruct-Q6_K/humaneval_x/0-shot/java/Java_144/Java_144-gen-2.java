The problem is asking to write a function that takes two string representations of fractions as input and returns true if the product of the two fractions is a whole number, and false otherwise.

Here is the solution in Java:

```java
public boolean simplify(String x, String n) {
    int[] xInt = parseFraction(x);
    int[] nInt = parseFraction(n);

    int productNumerator = xInt[0] * nInt[0];
    int productDenominator = xInt[1] * nInt[1];

    if (gcd(productNumerator, productDenominator) == 1) {
        return true;
    }

    return false;
}

public int[] parseFraction(String s) {
    String[] parts = s.split("/");
    return new int[]{Integer.parseInt(parts[0]), Integer.parseInt(parts[1])};
}

public int gcd(int a, int b) {
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}
```

In this solution, the `simplify` function first parses the input strings into integer arrays representing the numerator and denominator of the fractions. It then calculates the product of the two fractions by multiplying the numerators and denominators separately.

The `gcd` function is a helper function that calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

Finally, the `simplify` function returns true if the GCD of the product's numerator and denominator is 1, indicating that the product is a whole number. Otherwise, it returns false.