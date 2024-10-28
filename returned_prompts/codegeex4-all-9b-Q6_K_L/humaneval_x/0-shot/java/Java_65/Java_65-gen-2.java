Here is a Java solution for the problem:

```java
public String circularShift(int x, int shift) {
    String str = Integer.toString(x);
    int len = str.length();
    if (shift > len) {
        return new StringBuilder(str).reverse().toString();
    } else {
        return str.substring(len - shift) + str.substring(0, len - shift);
    }
}
```
This solution works by first converting the integer x to a string. Then, if the shift is greater than the length of the string, it returns the reversed string. Otherwise, it returns a new string that is the concatenation of the substring of the original string starting from len - shift to the end of the string and the substring of the original string from the start of the string to len - shift. This effectively shifts the digits of the integer to the right by the specified number of places.