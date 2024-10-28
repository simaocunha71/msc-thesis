Here is a simple solution in Java:

```java
import java.util.*;

class Solution {
    public String sortNumbers(String numbers) {
        // Split the numbers string into an array
        String[] nums = numbers.split(" ");
        // Create a list from the array
        List<Integer> numList = new ArrayList<>();
        // Loop through the array and convert each string to an integer and add it to the list
        for (String num : nums) {
            numList.add(Integer.parseInt(num));
        }
        // Sort the list
        Collections.sort(numList);
        // Convert the list back to a string
        StringBuilder sb = new StringBuilder();
        for (Integer num : numList) {
            sb.append(num).append(" ");
        }
        // Return the string without the trailing space
        return sb.toString().trim();
    }
}
```

This solution first splits the input string into an array of strings, then converts each string to an integer and adds it to a list. It then sorts the list and converts it back to a string, finally returning the string without the trailing space.