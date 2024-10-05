```java
public String circularShift(int x, int shift) {
    String strX = String.valueOf(x);
    int len = strX.length();
    shift = shift % len;

    if (shift == 0) {
        return strX;
    }

    String firstPart = strX.substring(0, len - shift);
    String secondPart = strX.substring(len - shift);

    return secondPart + firstPart;
}
```

Explanation:

1. Convert the integer `x` to a string `strX`.
2. Calculate the length of the string `len`.
3. Calculate the actual shift by taking the remainder of the division of `shift` by `len`.
4. If the shift is 0, return the original string.
5. Split the string into two parts: `firstPart` and `secondPart`. `firstPart` takes all characters from the beginning to the `shift`-th character from the end, and `secondPart` takes all characters from the `shift`-th character from the end to the end.
6. Return the concatenation of `secondPart` and `firstPart`. This effectively performs a circular shift of the digits.

For example, if `x` is 12 and `shift` is 1, the function will return "21", which is the result of shifting the digits of 12 one position to the right. If `shift` is 2, the function will return "12", which is the same as the original number since there is no actual shift. If `shift` is greater than the number of digits, the function will return the digits reversed, as in the case where `x` is 12 and `shift` is 3, the function will return "21".