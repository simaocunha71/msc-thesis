```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        if (arr == null || arr.isEmpty()) {
            return new ArrayList<>();
        }
        List<Integer> sorted = new ArrayList<>(arr);
        Collections.sort(sorted);
        List<Integer> filtered = new ArrayList<>();
        for (Integer i : sorted) {
            if (i >= 1 && i <= 9) {
                filtered.add(i);
            }
        }
        Collections.reverse(filtered);
        List<String> result = new ArrayList<>();
        for (Integer i : filtered) {
            result.add(getNumberName(i));
        }
        return result;
    }

    private String getNumberName(int number) {
        switch (number) {
            case 1:
                return "One";
            case 2:
                return "Two";
            case 3:
                return "Three";
            case 4:
                return "Four";
            case 5:
                return "Five";
            case 6:
                return "Six";
            case 7:
                return "Seven";
            case 8:
                return "Eight";
            case 9:
                return "Nine";
            default:
                return "";
        }
    }
}
```
