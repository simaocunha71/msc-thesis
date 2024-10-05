Here is a Java solution using the `stream()` function and the `filter()` function:

```java
public List<Integer> uniqueDigits(List<Integer> x) {
    return x.stream()
            .filter(num -> num.toString().chars().allMatch(ch -> ch % 2 != 0))
            .sorted()
            .collect(Collectors.toList());
}
```

Here's what the code does:
- `x.stream()` converts the list `x` into a stream.
- `.filter(num -> num.toString().chars().allMatch(ch -> ch % 2 != 0))` filters out the numbers that have any even digit.
  - `num.toString().chars()` converts the number `num` to a string and then converts the string to a stream of characters.
  - `.allMatch(ch -> ch % 2 != 0)` checks if all characters in the stream are odd (i.e., do not have any even digit).
- `.sorted()` sorts the remaining numbers in increasing order.
- `.collect(Collectors.toList())` converts the stream back into a list.

This solution is efficient as it uses Java 8's stream API to filter and sort the numbers in a single pass.