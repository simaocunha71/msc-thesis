Here is the Java solution for the problem:

```java
public String intToMiniRoman(int number) {
    String[] romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int[] decimalValues = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    StringBuilder result = new StringBuilder();

    for (int i = 0; i < decimalValues.length; i++) {
        while (number >= decimalValues[i]) {
            number -= decimalValues[i];
            result.append(romanNumerals[i]);
        }
    }

    return result.toString().toLowerCase();
}
```
The function `intToMiniRoman` takes an integer `number` as an argument and converts it to its Roman numeral equivalent as a string, which is then returned in lowercase.

The Roman numeral system is represented by an array of strings `romanNumerals` and an array of integers `decimalValues`. The `romanNumerals` array contains the Roman numeral symbols and the `decimalValues` array contains their corresponding decimal values.

The function iterates over the `romanNumerals` and `decimalValues` arrays using a for loop. For each iteration, it checks if the `number` is greater than or equal to the current decimal value. If it is, it subtracts the decimal value from the `number` and appends the corresponding Roman numeral symbol to the `result` string. This process continues until the `number` becomes 0.

Finally, the function returns the `result` string as a lowercase Roman numeral equivalent of the input `number`.