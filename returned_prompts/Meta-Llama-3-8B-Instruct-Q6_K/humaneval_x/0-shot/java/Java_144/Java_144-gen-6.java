```java
import java.util.*;

class Solution {
    public boolean simplify(String x, String n) {
        // Parse the fractions
        int[] xParts = parseFraction(x);
        int[] nParts = parseFraction(n);

        // Calculate the product
        int numerator = xParts[0] * nParts[0];
        int denominator = xParts[1] * nParts[1];

        // Check if the product is a whole number
        if (denominator == 1) {
            return true;
        }

        // Calculate the greatest common divisor (GCD) of the numerator and denominator
        int gcd = getGCD(Math.abs(numerator), denominator);

        // Check if the GCD is equal to the numerator or denominator
        return gcd == numerator || gcd == denominator;
    }

    // Parse a fraction from a string
    private int[] parseFraction(String fraction) {
        String[] parts = fraction.split("/");
        int numerator = Integer.parseInt(parts[0]);
        int denominator = Integer.parseInt(parts[1]);
        return new int[] {numerator, denominator};
    }

    // Calculate the greatest common divisor (GCD) of two numbers
    private int getGCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
```

This solution first parses the input fractions into their numerator and denominator parts. Then, it calculates the product of the two fractions and checks if the denominator is equal to 1, which would indicate that the product is a whole number. If the denominator is not 1, the solution calculates the greatest common divisor (GCD) of the numerator and denominator using the Euclidean algorithm. Finally, it checks if the GCD is equal to the numerator or denominator, which would indicate that the product is a whole number. If the GCD is equal to either the numerator or denominator, the function returns true, indicating that the product is a whole number; otherwise, it returns false.