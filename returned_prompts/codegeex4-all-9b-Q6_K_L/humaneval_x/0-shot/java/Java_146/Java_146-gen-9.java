```java
public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && isOddFirstAndLastDigit(num)) {
            count++;
        }
    }
    return count;
}

private boolean isOddFirstAndLastDigit(int num) {
    int firstDigit = Math.abs(num) % 10;
    int lastDigit = Math.abs(num) / 10 % 10;
    return firstDigit % 2 != 0 && lastDigit % 2 != 0;
}
```
The `specialFilter` function iterates through the input list and checks if each number is greater than 10 and both its first and last digits are odd. It uses the `isOddFirstAndLastDigit` helper function to determine if a number has odd first and last digits. If both conditions are true, the count is incremented. Finally, the function returns the count.