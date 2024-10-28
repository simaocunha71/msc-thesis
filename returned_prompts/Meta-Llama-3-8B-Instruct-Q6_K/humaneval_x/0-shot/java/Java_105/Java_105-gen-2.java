Here is the solution:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                result.add(getNumberName(num));
            }
        }
        Collections.sort(result);
        Collections.reverse(result);
        return result;
    }

    private String getNumberName(int num) {
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

This solution first filters out the numbers between 1 and 9, then sorts the filtered numbers and reverses the order. It then maps each number to its corresponding name and returns the result as a list of strings. If the input array is empty, it returns an empty list. If the array contains any numbers outside the range 1-9, they are simply ignored. The method `getNumberName(int num)` is a helper method that maps a number to its corresponding name. It uses a switch statement to achieve this.