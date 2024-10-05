```java
import java.util.*;

class Solution {
    private static final Map<Integer, String> romanMap = new HashMap<>();
    static {
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
    }

    public String intToMiniRoman(int number) {
        StringBuilder roman = new StringBuilder();
        for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
            while (number >= entry.getKey()) {
                number -= entry.getKey();
                roman.append(entry.getValue());
            }
        }
        return roman.toString().toLowerCase();
    }
}
```

The problem is asking to convert an integer to its Roman numeral equivalent. We can use a map to store the Roman numerals and their corresponding integer values. Then, we iterate through the map and subtract the integer value from the input number as long as it's greater than or equal to the value. We append the corresponding Roman numeral to the result string. Finally, we return the result string in lowercase.

The time complexity is O(1) because we are iterating through a constant-sized map. The space complexity is also O(1) because we are using a constant amount of space to store the map and the result string.