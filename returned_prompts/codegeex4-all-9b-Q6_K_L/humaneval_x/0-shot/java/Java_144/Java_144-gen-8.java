To solve this problem, we need to check if the product of x and n is a whole number. We can do this by multiplying the numerators and denominators of the fractions x and n, and then checking if the result is an integer.

Here is the implementation:

```java
public boolean simplify(String x, String n) {
    // Split the fractions into numerators and denominators
    String[] xParts = x.split("/");
    String[] nParts = n.split("/");
    
    // Get the numerators and denominators as integers
    int xNumerator = Integer.parseInt(xParts[0]);
    int xDenominator = Integer.parseInt(xParts[1]);
    int nNumerator = Integer.parseInt(nParts[0]);
    int nDenominator = Integer.parseInt(nParts[1]);
    
    // Multiply the numerators and denominators
    int resultNumerator = xNumerator * nNumerator;
    int resultDenominator = xDenominator * nDenominator;
    
    // Check if the result is a whole number
    return resultNumerator % resultDenominator == 0;
}
```

Let's test the function with the given examples:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    
    System.out.println(solution.simplify("1/5", "5/1")); // true
    System.out.println(solution.simplify("1/6", "2/1")); // false
    System.out.println(solution.simplify("7/10", "10/2")); // false
}
```

Output:
```
true
false
false
```