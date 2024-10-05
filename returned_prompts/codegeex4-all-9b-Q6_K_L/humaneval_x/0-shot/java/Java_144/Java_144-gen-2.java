To simplify the expression `x * n`, we need to multiply the numerators and denominators of the fractions. Then, we check if the resulting fraction is a whole number.

Here is the implementation of the `simplify` function in Java:

```java
public boolean simplify(String x, String n) {
    // Split the fractions into numerators and denominators
    String[] xParts = x.split("/");
    String[] nParts = n.split("/");
    
    // Parse the numerators and denominators
    int xNum = Integer.parseInt(xParts[0]);
    int xDen = Integer.parseInt(xParts[1]);
    int nNum = Integer.parseInt(nParts[0]);
    int nDen = Integer.parseInt(nParts[1]);
    
    // Multiply the numerators and denominators
    int num = xNum * nNum;
    int den = xDen * nDen;
    
    // Check if the resulting fraction is a whole number
    return num % den == 0;
}
```

In this implementation, we split the fractions `x` and `n` into their numerators and denominators using the `split` method. Then, we parse the numerators and denominators into integers using the `parseInt` method.

Next, we multiply the numerators and denominators to get the numerator and denominator of the resulting fraction.

Finally, we check if the resulting fraction is a whole number by checking if the remainder of the division of the numerator by the denominator is zero. If it is, the function returns `true`, indicating that the expression `x * n` evaluates to a whole number. Otherwise, it returns `false`.