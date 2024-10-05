Here is a possible solution in Java:

```java
public int doubleTheDifference(List<Object> lst) {
    int sum = 0;
    for (Object obj : lst) {
        if (obj instanceof Integer && (Integer) obj > 0 && (Integer) obj % 2 != 0) {
            sum += Math.pow((Integer) obj, 2);
        }
    }
    return sum;
}
```

Explanation:

- We initialize a variable `sum` to 0 to keep track of the sum of squares of odd numbers.
- We loop through each object `obj` in the list `lst`.
- We check if `obj` is an instance of `Integer`, it is greater than 0, and it is odd (i.e., `obj % 2 != 0`).
- If all these conditions are true, we add the square of `obj` to `sum` using the `Math.pow()` method.
- Finally, we return `sum`, which is the sum of squares of odd numbers.