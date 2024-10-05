You can solve this problem by using the `instanceof` operator to check if the given objects are `Integer` or not. If they are, then you can convert them to `int` type and check if any of the numbers is equal to the sum of the other two.

Here is the solution:

```java
public boolean anyInt(Object x, Object y, Object z) {
    if (x instanceof Integer && y instanceof Integer && z instanceof Integer) {
        int a = (int) x;
        int b = (int) y;
        int c = (int) z;
        return a == b + c || b == a + c || c == a + b;
    }
    return false;
}
```

In this solution, we first check if all three objects are `Integer` using the `instanceof` operator. If they are, then we convert them to `int` type and check if any of the numbers is equal to the sum of the other two. If any of the numbers is equal to the sum of the other two, we return `true`, otherwise we return `false`. If any of the objects is not `Integer`, we return `false`.