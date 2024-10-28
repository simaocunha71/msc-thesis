```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        if (arr.size() == 0) {
            return new ArrayList<>();
        }
        arr.removeIf(n -> n < 1 || n > 9);
        Collections.sort(arr);
        Collections.reverse(arr);
        List<String> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i++) {
            result.add(numToWord(arr.get(i)));
        }
        return result;
    }

    private String numToWord(int num) {
        switch (num) {
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