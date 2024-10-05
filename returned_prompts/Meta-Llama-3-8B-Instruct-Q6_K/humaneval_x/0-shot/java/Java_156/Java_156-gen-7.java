Here is a Java solution using a HashMap to store the Roman numerals and their corresponding integer values. We then use a while loop to convert the integer to Roman numeral.

```java
import java.util.*;

class Solution {
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

        StringBuilder roman = new StringBuilder();
        while (number > 0) {
            for (Map.Entry<Integer, String> entry : romanMap.entrySet()) {
                while (number >= entry.getKey()) {
                    roman.append(entry.getValue());
                    number -= entry.getKey();
                }
            }
        }
        return roman.toString().toLowerCase();
    }
}
```
This solution works by iterating over the map and appending the Roman numeral to the result string as many times as the number is greater than or equal to the corresponding integer value. The number is then updated by subtracting the integer value from the map. This process continues until the number becomes 0. Finally, the result string is converted to lowercase and returned. 