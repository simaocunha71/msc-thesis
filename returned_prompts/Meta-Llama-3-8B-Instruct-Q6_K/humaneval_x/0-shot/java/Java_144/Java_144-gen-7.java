The problem is asking you to write a function that takes two string representations of fractions (x and n) and returns true if the product of x and n is a whole number, and false otherwise.

Here is a possible solution in Java:
```java
public boolean simplify(String x, String n) {
    int[] xy = parseFraction(x);
    int[] yn = parseFraction(n);

    int numerator = xy[0] * yn[0];
    int denominator = xy[1] * yn[1];

    return gcd(numerator, denominator) == 1;
}

private int[] parseFraction(String s) {
    String[] parts = s.split("/");
    int numerator = Integer.parseInt(parts[0]);
    int denominator = Integer.parseInt(parts[1]);
    return new int[]{numerator, denominator};
}

private int gcd(int a, int b) {
    if (b == 0) {
        return a;
    } else {
        return gcd(b, a % b);
    }
}
```
The `parseFraction` method splits the input string into numerator and denominator, and returns them as an array. The `gcd` method calculates the greatest common divisor of two numbers using the Euclidean algorithm.

The `simplify` method parses the input strings, calculates the product of the fractions, and checks if the numerator and denominator are coprime (i.e., their greatest common divisor is 1). If they are, it returns true, otherwise it returns false.