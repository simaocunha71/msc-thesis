Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> sortedArr = new ArrayList<>();

        // Filter out numbers that are not between 1 and 9
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sortedArr.add(num);
            }
        }

        // Sort the array
        Collections.sort(sortedArr);

        // Reverse the array
        Collections.reverse(sortedArr);

        // Convert each number to its corresponding name
        for (int num : sortedArr) {
            switch (num) {
                case 1:
                    result.add("One");
                    break;
                case 2:
                    result.add("Two");
                    break;
                case 3:
                    result.add("Three");
                    break;
                case 4:
                    result.add("Four");
                    break;
                case 5:
                    result.add("Five");
                    break;
                case 6:
                    result.add("Six");
                    break;
                case 7:
                    result.add("Seven");
                    break;
                case 8:
                    result.add("Eight");
                    break;
                case 9:
                    result.add("Nine");
                    break;
            }
        }

        return result;
    }
}
```

This solution first filters out the numbers that are not between 1 and 9. Then it sorts the array and reverses it. Finally, it converts each number to its corresponding name and adds it to the result list. The result list is then returned. If the input array is empty, an empty list is returned. If the array has any numbers outside the range of 1 to 9, they are ignored. The solution is case-sensitive, so "One" is treated as a different string from "one". If you want to make the solution case-insensitive, you can convert the input array to lower case or upper case before processing it.