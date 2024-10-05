```java
public String intToMiniRoman(int number) {
    String[] romanValues = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    int[] romanNumbers = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    StringBuilder result = new StringBuilder();

    for (int i = 0; i < romanNumbers.length; i++) {
        while (number >= romanNumbers[i]) {
            number -= romanNumbers[i];
            result.append(romanValues[i]);
        }
    }

    return result.toString().toLowerCase();
}
```
Explanation:
This Java function converts an integer to its Roman numeral equivalent. It uses two arrays: `romanValues` for the Roman numeral symbols and `romanNumbers` for the corresponding integer values.

It then iterates over the arrays, subtracting the largest possible Roman numeral value from the input number and appending the corresponding Roman numeral symbol to the result. This process repeats until the input number becomes 0.

Finally, the function returns the resulting Roman numeral string in lowercase. The `toLowerCase()` method is used to ensure the output is in lowercase, as per the problem requirements.