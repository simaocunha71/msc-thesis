```java
public int countNums(List<Integer> arr) {
    return (int) arr.stream()
            .filter(x -> sumDigits(Math.abs(x)) > 0)
            .count();
}

private int sumDigits(int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}
```