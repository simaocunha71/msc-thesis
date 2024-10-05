Here is a Java solution using a combination of sorting, reversing, and mapping:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> sortedArr = new ArrayList<>();

        // Filter out numbers outside the range [1, 9]
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sortedArr.add(num);
            }
        }

        // Sort the filtered array
        sortedArr.sort(Comparator.naturalOrder());

        // Reverse the sorted array
        Collections.reverse(sortedArr);

        // Map the numbers to their corresponding names
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

This solution first filters out the numbers outside the range [1, 9], then sorts the filtered array, reverses it, and finally maps the numbers to their corresponding names. The result is a list of strings representing the numbers in the original array, with each number replaced by its corresponding name. If the array is empty, the method returns an empty list. If the array contains any numbers outside the range [1, 9], they are ignored.