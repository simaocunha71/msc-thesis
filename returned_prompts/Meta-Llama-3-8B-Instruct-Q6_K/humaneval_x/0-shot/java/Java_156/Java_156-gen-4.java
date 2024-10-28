```java
import java.util.*;

public class Solution {
    public String intToMiniRoman(int number) {
        Map<Integer, String> romanMap = new HashMap<>();
        romanMap.put(1000, "m");
        romanMap.put(900, "cm");
        romanMap.put(500, "d");
        romanMap.put(400, "cd");
        romanMap.put(100, "c");
        romanMap.put(90, "xc");
        romanMap.put(50, "l");
        romanMap.put(40, "xl");
        romanMap.put(10, "x");
        romanMap.put(9, "ix");
        romanMap.put(5, "v");
        romanMap.put(4, "iv");
        romanMap.put(1, "i");

        StringBuilder result = new StringBuilder();
        for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
            while (number >= entry.getKey()) {
                result.append(entry.getValue());
                number -= entry.getKey();
            }
        }
        return result.toString().toLowerCase();
    }
}
```
The provided solution uses a map to store the roman numerals and their corresponding integer values. It iterates through the map and appends the roman numeral to the result string if the number is greater than or equal to the integer value. It then subtracts the integer value from the number and continues the process until the number becomes 0. Finally, it converts the result string to lowercase and returns it.

The time complexity of this solution is O(1) because it only iterates through a fixed-size map, and the space complexity is also O(1) because it only uses a constant amount of space to store the result string.