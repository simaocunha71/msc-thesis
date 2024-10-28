Here is a Java solution that uses a for-each loop to iterate over the list and a series of if statements to check the conditions:

```java
public int specialFilter(List<Integer> nums) {
    int count = 0;
    for (int num : nums) {
        if (num > 10 && num % 2 != 0) {
            int firstDigit = Integer.parseInt(String.valueOf(num).charAt(0) + "");
            int lastDigit = Integer.parseInt(String.valueOf(num).charAt(String.valueOf(num).length() - 1) + "");
            if (firstDigit % 2 != 0 && lastDigit % 2 != 0) {
                count++;
            }
        }
    }
    return count;
}
```

This function works by first checking if the number is greater than 10 and odd. If it is, it then checks if the first and last digits are both odd. If both conditions are met, it increments the count.

The function uses the `parseInt` method to convert the first and last characters of the number to integers, and then checks if they are both odd.

The time complexity of this function is O(n), where n is the size of the input list. This is because it needs to iterate over the entire list once.