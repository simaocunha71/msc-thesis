Here is the Java solution for the problem:

```java
public int countNums(List<Integer> arr) {
    int count = 0;
    for (int num : arr) {
        int sum = getSumOfDigits(num);
        if (sum > 0) {
            count++;
        }
    }
    return count;
}

private int getSumOfDigits(int num) {
    int sum = 0;
    while (num != 0) {
        int digit = num % 10;
        if (num < 0) {
            digit = -digit;
        }
        sum += digit;
        num /= 10;
    }
    return sum;
}
```

Explanation:
The problem requires to count the numbers in the array whose sum of digits is greater than 0. We can do this by iterating over each number in the array, calculating the sum of its digits using the `getSumOfDigits` method, and incrementing the count if the sum is greater than 0.

The `getSumOfDigits` method calculates the sum of digits of a number. It uses a while loop to extract each digit from the number, and adds it to the sum. If the number is negative, it makes the digit negative as well. The sum is then returned.

In the `countNums` method, we iterate over each number in the array, calculate its sum of digits, and increment the count if the sum is greater than 0. Finally, we return the count.