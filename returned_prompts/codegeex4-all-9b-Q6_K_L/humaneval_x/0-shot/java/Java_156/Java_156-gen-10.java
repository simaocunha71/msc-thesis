```java
import java.util.*;
import java.lang.*;

class Solution {
    public String intToMiniRoman(int number) {
        // Create a list of Roman numerals and their corresponding integer values
        List<int[]> numerals = new ArrayList<>();
        numerals.add(new int[]{1000, 'm'});
        numerals.add(new int[]{900, 'cm'});
        numerals.add(new int[]{500, 'd'});
        numerals.add(new int[]{400, 'cd'});
        numerals.add(new int[]{100, 'c'});
        numerals.add(new int[]{90, 'xc'});
        numerals.add(new int[]{50, 'l'});
        numerals.add(new int[]{40, 'xl'});
        numerals.add(new int[]{10, 'x'});
        numerals.add(new int[]{9, 'ix'});
        numerals.add(new int[]{5, 'v'});
        numerals.add(new int[]{4, 'iv'});
        numerals.add(new int[]{1, 'i'});

        // Initialize the result string
        StringBuilder roman = new StringBuilder();

        // Iterate through the list of Roman numerals and add them to the result string
        for (int[] n : numerals) {
            while (number >= n[0]) {
                roman.append((char) n[1]);
                number -= n[0];
            }
        }

        // Return the result string
        return roman.toString();
    }
}
```