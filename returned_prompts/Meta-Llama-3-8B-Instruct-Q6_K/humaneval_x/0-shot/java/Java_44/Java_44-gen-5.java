The problem is asking for a function that converts a given integer `x` to a different base, specified by `base`. The base should be less than 10, and the function should return a string representation of the converted number.

Here is a Java solution for the problem:
```java
public String changeBase(int x, int base) {
    StringBuilder sb = new StringBuilder();
    while (x > 0) {
        int remainder = x % base;
        if (remainder < 10) {
            sb.insert(0, (char) (remainder + '0'));
        } else {
            sb.insert(0, (char) (remainder + 'a' - 10));
        }
        x /= base;
    }
    return sb.toString();
}
```
Here's an explanation of the code:

1. We use a `StringBuilder` object `sb` to build the resulting string.
2. We use a while loop to repeatedly divide the input number `x` by the base `base`, and calculate the remainder.
3. If the remainder is less than 10, we convert it to a character by adding the ASCII value of '0' to the remainder. This is because the characters '0' to '9' have ASCII values 48 to 57, respectively.
4. If the remainder is 10 or greater, we convert it to a character by adding the ASCII value of 'a' minus 10 to the remainder. This is because the characters 'a' to 'z' have ASCII values 97 to 122, respectively.
5. We insert the resulting character at the beginning of the `StringBuilder` object `sb` using the `insert(0, char)` method.
6. We repeat steps 2-5 until `x` becomes 0.
7. Finally, we return the resulting string by calling the `toString()` method on the `StringBuilder` object `sb`.

You can test this function with different inputs to verify its correctness. For example:
```java
System.out.println(changeBase(8, 3)); // Output: "22"
System.out.println(changeBase(8, 2)); // Output: "1000"
System.out.println(changeBase(7, 2)); // Output: "111"
``` 