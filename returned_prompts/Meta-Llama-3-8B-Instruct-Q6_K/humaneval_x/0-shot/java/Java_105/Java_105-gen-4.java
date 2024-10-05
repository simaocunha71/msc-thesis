Here is the Java code for the problem:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> nums = new ArrayList<>();
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                nums.add(num);
            }
        }
        if (nums.isEmpty()) {
            return new ArrayList<>();
        }
        Collections.sort(nums);
        List<String> result = new ArrayList<>();
        for (int i = nums.size() - 1; i >= 0; i--) {
            result.add(getNumberName(nums.get(i)));
        }
        return result;
    }

    public String getNumberName(int num) {
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

This solution first filters out the numbers outside the range 1 to 9, then sorts the remaining numbers, reverses the sorted list, and finally converts each number to its corresponding name. The `getNumberName` method is used to convert a number to its corresponding name. If the input array is empty, an empty array is returned. If the array contains any numbers outside the range 1 to 9, they are ignored. The result is a list of strings, where each string is the name of a number in the range 1 to 9. The numbers are in descending order. If a number is outside the range 1 to 9, its name is not included in the result. The result does not include any number names that are not in the range 1 to 9. If the input array is empty, the result is an empty array. If the array contains any numbers outside the range 1 to 9, the result includes only the names of numbers in the range 1 to 9. The result includes the names of all numbers in the range 1 to 9. The numbers are in descending order. The result does not include any number names that are not in the range 1 to 9. The result includes the names of numbers in the range