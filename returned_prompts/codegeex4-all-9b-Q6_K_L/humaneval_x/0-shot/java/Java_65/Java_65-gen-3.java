Here is a Java solution for the problem. This solution converts the integer to a string, then splits the string into an array of characters. It then performs a circular shift on the array, and finally joins the array back into a string to return the result.

```java
public String circularShift(int x, int shift) {
    String numStr = String.valueOf(x);
    int len = numStr.length();
    if (shift > len) {
        return new StringBuilder(numStr).reverse().toString();
    }
    char[] numArr = numStr.toCharArray();
    int shiftBy = len - shift;
    char[] shiftedArr = new char[len];
    System.arraycopy(numArr, shiftBy, shiftedArr, 0, len - shiftBy);
    System.arraycopy(numArr, 0, shiftedArr, len - shiftBy, shiftBy);
    return new String(shiftedArr);
}
```

This solution works by first checking if the shift is greater than the length of the number. If it is, it simply reverses the number and returns it. If not, it converts the number to a character array and performs a circular shift by copying the appropriate parts of the array to the new array. Finally, it converts the new array back to a string and returns it.