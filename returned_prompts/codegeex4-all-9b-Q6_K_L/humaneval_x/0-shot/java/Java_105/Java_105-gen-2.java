```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        // sort the array
        Collections.sort(arr);
        // reverse the array
        Collections.reverse(arr);
        // create a list to store the result
        List<String> result = new ArrayList<>();
        // create a map to store the digit names
        Map<Integer, String> digitNames = new HashMap<>();
        digitNames.put(1, "One");
        digitNames.put(2, "Two");
        digitNames.put(3, "Three");
        digitNames.put(4, "Four");
        digitNames.put(5, "Five");
        digitNames.put(6, "Six");
        digitNames.put(7, "Seven");
        digitNames.put(8, "Eight");
        digitNames.put(9, "Nine");
        // iterate over the array
        for (int num : arr) {
            // if the number is between 1 and 9 inclusive, add its name to the result
            if (num >= 1 && num <= 9) {
                result.add(digitNames.get(num));
            }
        }
        // return the result
        return result;
    }
}
```