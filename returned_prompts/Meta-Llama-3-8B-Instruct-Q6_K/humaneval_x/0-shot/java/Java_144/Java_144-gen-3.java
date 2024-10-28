The problem is asking to write a function that simplifies two fractions x and n, and checks if their product is a whole number. The function should return true if the product is a whole number and false otherwise.

Here is the solution in Java:
```java
public boolean simplify(String x, String n) {
    int num1 = getNum(x);
    int denom1 = getDenom(x);
    int num2 = getNum(n);
    int denom2 = getDenom(n);

    int common = gcd(denom1, denom2);
    int newNum1 = num1 * (denom2 / common);
    int newDenom1 = denom1 / common;
    int newNum2 = num2 * (denom1 / common);
    int newDenom2 = denom2 / common;

    int productNum = newNum1 * newNum2;
    int productDenom = newDenom1 * newDenom2;

    return productNum == productDenom;
}

private int getNum(String s) {
    String[] parts = s.split("/");
    return Integer.parseInt(parts[0]);
}

private int getDenom(String s) {
    String[] parts = s.split("/");
    return Integer.parseInt(parts[1]);
}

private int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}
```
The `simplify` function takes two strings representing fractions x and n, and returns a boolean indicating whether their product is a whole number.

The function first extracts the numerators and denominators from the input strings using the `getNum` and `getDenom` functions.

It then calculates the greatest common divisor (GCD) of the denominators using the `gcd` function.

The function then simplifies the fractions by dividing both numerators and denominators by the GCD.

Finally, it calculates the product of the simplified fractions and checks if it is equal to a whole number. If it is, the function returns true; otherwise, it returns false.