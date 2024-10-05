The problem is asking to write a function that simplifies two fractions (x and n) and checks if their product is a whole number. The function takes two string parameters, x and n, in the format of "numerator/denominator" where both the numerator and denominator are positive whole numbers. The function should return true if the product of x and n is a whole number, and false otherwise.

Here is the solution for the problem:

```java
public boolean simplify(String x, String n) {
    int numeratorX = getNumerator(x);
    int denominatorX = getDenominator(x);
    int numeratorN = getNumerator(n);
    int denominatorN = getDenominator(n);

    int numeratorProduct = numeratorX * numeratorN;
    int denominatorProduct = denominatorX * denominatorN;

    return gcd(denominatorProduct, numeratorProduct) == 1;
}

private int getNumerator(String fraction) {
    String[] parts = fraction.split("/");
    return Integer.parseInt(parts[0]);
}

private int getDenominator(String fraction) {
    String[] parts = fraction.split("/");
    return Integer.parseInt(parts[1]);
}

private int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
```

In this solution, the `getNumerator` and `getDenominator` methods are used to extract the numerator and denominator from the input strings. The `gcd` method is used to calculate the greatest common divisor of the numerator and denominator of the product of the two fractions. If the gcd is 1, then the product is a whole number, and the function returns true. Otherwise, it returns false. The `gcd` method uses the Euclidean algorithm to calculate the gcd of two numbers. It recursively calls itself with the second number and the remainder of the division of the first number by the second, until the second number is 0. At that point, it returns the first number, which is the gcd of the original two numbers.