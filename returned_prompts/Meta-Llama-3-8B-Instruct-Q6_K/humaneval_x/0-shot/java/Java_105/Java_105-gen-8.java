Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> sortedArr = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sortedArr.add(num);
            }
        }
        if (sortedArr.isEmpty()) {
            return result;
        }
        Collections.sort(sortedArr);
        Collections.reverse(sortedArr);
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
This solution sorts the array of integers that are between 1 and 9, reverses the resulting array, and then replaces each digit by its corresponding name. If the array is empty, the solution returns an empty array. If the array has any numbers outside the range of 1 to 9, they are ignored. The solution uses Java's built-in sorting and reversing functions, as well as a switch statement to convert the numbers to their corresponding names. The solution returns a list of strings, where each string is the name of a number in the original array.