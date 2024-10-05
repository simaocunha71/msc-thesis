Here is a Java solution for the problem:

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
    if (num < 0) {
        num = -num;
    }
    while (num > 0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}
```

This solution defines a helper method `getSumOfDigits` to calculate the sum of digits of a number. It takes into account negative numbers by converting them to positive at the beginning. The main method `countNums` iterates over the input array, calculates the sum of digits for each number, and increments the count if the sum is greater than 0. The method returns the total count.