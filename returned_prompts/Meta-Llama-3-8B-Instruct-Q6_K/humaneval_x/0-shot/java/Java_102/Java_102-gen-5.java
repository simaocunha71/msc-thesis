Here is a Java function that implements the described behavior:

```java
public int chooseNum(int x, int y) {
    if (x > y) {
        int temp = x;
        x = y;
        y = temp;
    }
    for (int i = x; i <= y; i++) {
        if (i % 2 == 0) {
            return i;
        }
    }
    return -1;
}
```

This function first ensures that `x` is the smaller number and `y` is the larger number. Then it iterates over the range `[x, y]` and returns the first even number it encounters. If no even number is found, it returns `-1`.