To convert an integer to its Roman numeral equivalent, we can use a HashMap to map each decimal value to its corresponding Roman numeral. We can then iterate through the integer, subtracting the decimal value of each Roman numeral until the integer is zero. The resulting string will be the Roman numeral equivalent of the integer.

Here is the updated code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intToMiniRoman(int number) {
        Map<Integer, String> romanMap = new HashMap<>();
        romanMap.put(1, "i");
        romanMap.put(4, "iv");
        romanMap.put(5, "v");
        romanMap.put(9, "ix");
        romanMap.put(10, "x");
        romanMap.put(40, "xl");
        romanMap.put(50, "l");
        romanMap.put(90, "xc");
        romanMap.put(100, "c");
        romanMap.put(400, "cd");
        romanMap.put(500, "d");
        romanMap.put(900, "cm");
        romanMap.put(1000, "m");

        String romanNumeral = "";
        for (int i = 1000; i >= 1; i /= 10) {
            int digit = number / i;
            if (digit > 0) {
                romanNumeral += romanMap.get(i * digit);
                number -= i * digit;
            }
        }
        return romanNumeral;
    }
}
```