Here is a simple solution in Java. The main idea is to find the smallest even number in the range [x, y] and return it if it exists. If not, return -1.

```java
public int chooseNum(int x, int y) {
    if (x > y) return -1;
    if (x % 2 != 0) x++;
    if (x > y) return -1;
    return x;
}
```

This solution works by first checking if `x` is greater than `y`. If it is, then there are no even numbers in the range, so we return -1.

Next, we check if `x` is odd. If it is, we increment `x` by 1 to make it even.

Then, we check again if `x` is greater than `y`. If it is, then there are no even numbers in the range, so we return -1.

Finally, we return `x`, which is the smallest even number in the range [x, y].