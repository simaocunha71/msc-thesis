Here is a possible solution in Java:

```java
public int chooseNum(int x, int y) {
    // Check if x and y are both even
    if (x % 2 == 0 && y % 2 == 0) {
        // If y is less than x, then there's no even number in the range [x, y]
        if (y < x) {
            return -1;
        }
        // Otherwise, return the biggest even number in the range [x, y]
        return y;
    }
    // Check if x and y are both odd
    else if (x % 2 != 0 && y % 2 != 0) {
        // If y is less than x, then there's no even number in the range [x, y]
        if (y < x) {
            return -1;
        }
        // Otherwise, return the biggest even number in the range [x, y]
        return y - 1;
    }
    // Check if x is even and y is odd
    else if (x % 2 == 0 && y % 2 != 0) {
        // If y is less than x, then there's no even number in the range [x, y]
        if (y < x) {
            return -1;
        }
        // Otherwise, return the biggest even number in the range [x, y]
        return y;
    }
    // Check if x is odd and y is even
    else if (x % 2 != 0 && y % 2 == 0) {
        // If y is less than x + 1, then there's no even number in the range [x, y]
        if (y < x + 1) {
            return -1;
        }
        // Otherwise, return the biggest even number in the range [x, y]
        return y - 1;
    }
    // If none of the above conditions are met, then return -1
    return -1;
}
```

This solution checks if x and y are both even, both odd, or one is even and the other is odd. It then returns the biggest even number in the range [x, y] or -1 if there's no such number.