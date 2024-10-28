```java
public String changeBase(int x, int base) {
    StringBuilder sb = new StringBuilder();
    while (x > 0) {
        int remainder = x % base;
        sb.insert(0, remainder);
        x = x / base;
    }
    return sb.toString();
}
```

Explanation:
The problem is asking to convert a given number `x` to a different base. The base is given as an input and it is less than 10.

Here's a simple solution using a StringBuilder to build the result string from left to right.

1. Create a StringBuilder object `sb` to store the result.
2. Loop until `x` becomes 0.
3. In each iteration, calculate the remainder of `x` divided by the base using the modulo operator (`%`). This gives the last digit of the result.
4. Insert the remainder at the beginning of the StringBuilder using the `insert(0, remainder)` method.
5. Update `x` by dividing it by the base using integer division (`/`).
6. Repeat steps 3-5 until `x` becomes 0.
7. Return the result string using the `toString()` method of the StringBuilder.

This solution works by repeatedly dividing the input number by the base and appending the remainder to the result string. The result string is built from left to right, with the most significant digit first. This approach is efficient and easy to implement.

For example, if the input number is 8 and the base is 3, the result would be "22". If the base is 2, the result would be "1000". If the base is 2 and the input number is 7, the result would be "111".