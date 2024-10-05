```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        if (arr.size() == 0) {
            return new ArrayList<String>();
        }

        List<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= 1 && arr.get(i) <= 9) {
                result.add(arr.get(i));
            }
        }

        Collections.sort(result);

        Collections.reverse(result);

        List<String> resultString = new ArrayList<String>();

        for (int i = 0; i < result.size(); i++) {
            resultString.add(numberToWord(result.get(i)));
        }

        return resultString;
    }

    public String numberToWord(int num) {
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