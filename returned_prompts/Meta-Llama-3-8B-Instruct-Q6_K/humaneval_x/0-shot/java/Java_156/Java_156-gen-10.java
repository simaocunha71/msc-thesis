```java
public String intToMiniRoman(int number) {
    String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < values.length; i++) {
        while (number >= values[i]) {
            number -= values[i];
            result.append(romans[i]);
        }
    }
    return result.toString().toLowerCase();
}
```

Explanation:
The problem is to convert an integer into its Roman numeral equivalent. We can achieve this by using an array of Roman numerals and their corresponding integer values.

We start by initializing an empty StringBuilder `result` to store the Roman numeral equivalent.

Then, we iterate through the array of Roman numerals and their values. For each value, we check if the input number is greater than or equal to the current value. If it is, we subtract the value from the number and append the corresponding Roman numeral to the `result` StringBuilder.

We repeat this process until the number becomes 0. Finally, we return the Roman numeral equivalent as a string in lowercase by calling the `toLowerCase()` method on the `result` StringBuilder.

This solution has a time complexity of O(n), where n is the number of Roman numerals in the array, since we iterate through the array once. The space complexity is O(1), as we only use a fixed amount of space to store the `result` StringBuilder and the arrays of Roman numerals and values.