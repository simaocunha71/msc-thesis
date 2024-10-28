```java
public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && isOdd(num) && isOddFirstAndLastDigit(num)) {
            count++;
        }
    }
    return count;
}

private boolean isOdd(int num) {
    return num % 2 != 0;
}

private boolean isOddFirstAndLastDigit(int num) {
    int firstDigit = Math.abs(num) / 10;
    int lastDigit = Math.abs(num) % 10;
    return isOdd(firstDigit) && isOdd(lastDigit);
}
```
Explanation:
The `specialFilter` function iterates through the input list of numbers and checks for each number if it is greater than 10, if the number is odd and if both the first and last digits of the number are odd. If all these conditions are met, the count is incremented. Finally, the count is returned as the result. The helper functions `isOdd` and `isOddFirstAndLastDigit` are used to check if a number is odd and if both the first and last digits of a number are odd, respectively.