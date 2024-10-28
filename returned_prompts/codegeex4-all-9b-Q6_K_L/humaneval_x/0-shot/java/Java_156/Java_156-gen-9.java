```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intToMiniRoman(int number) {
        // Define the roman numerals and their corresponding integer values
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};

        // Initialize the result string
        StringBuilder result = new StringBuilder();

        // Iterate through the values and symbols arrays
        for (int i = 0; i < values.length; i++) {
            // While the number is greater than or equal to the current value
            while (number >= values[i]) {
                // Append the corresponding symbol to the result string
                result.append(symbols[i]);
                // Subtract the value from the number
                number -= values[i];
            }
        }

        // Return the result string
        return result.toString();
    }
}
```