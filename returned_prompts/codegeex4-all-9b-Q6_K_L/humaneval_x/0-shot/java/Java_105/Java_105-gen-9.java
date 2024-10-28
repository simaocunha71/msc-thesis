```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        if (arr.isEmpty()) {
            return result;
        }

        // Sort the array
        Collections.sort(arr);

        // Reverse the array
        Collections.reverse(arr);

        // Replace each digit by its corresponding name
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                result.add(numToWord(num));
            }
        }

        return result;
    }

    private String numToWord(int num) {
        switch (num) {
            case 1: return "One";
            case 2: return "Two";
            case 3: return "Three";
            case 4: return "Four";
            case 5: return "Five";
            case 6: return "Six";
            case 7: return "Seven";
            case 8: return "Eight";
            case 9: return "Nine";
            default: return "";
        }
    }
}
```