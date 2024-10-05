Here is a simple Java solution for the problem:

```java
public int chooseNum(int x, int y) {
    if (y < x) {
        return -1;
    }
    if (x % 2 == 1) {
        x++;
    }
    if (x > y) {
        return -1;
    }
    return x;
}
```
This function first checks if `y` is less than `x`, if so it returns `-1` because there are no even numbers between `x` and `y` (inclusive). Then it checks if `x` is odd, if so it increments `x` by 1 to make it even. After that it checks if `x` is greater than `y` and if so it returns `-1`. Finally it returns `x` because `x` is now the smallest even number in the range [x, y] inclusive.