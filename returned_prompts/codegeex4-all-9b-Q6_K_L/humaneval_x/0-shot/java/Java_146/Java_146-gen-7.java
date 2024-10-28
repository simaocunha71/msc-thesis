```java
public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && num % 2 != 0 && isOddDigit(num)) {
            count++;
        }
    }
    return count;
}

private boolean isOddDigit(int num) {
    int firstDigit = Math.abs(num) % 10;
    int lastDigit = num % 10;
    return firstDigit % 2 != 0 && lastDigit % 2 != 0;
}
```
This solution iterates through the list of numbers and checks each number to see if it is greater than 10 and if both its first and last digits are odd. If both conditions are met, the count is incremented. The `isOddDigit` method is used to check if both the first and last digits of a number are odd. The solution returns the count of numbers that meet the conditions.