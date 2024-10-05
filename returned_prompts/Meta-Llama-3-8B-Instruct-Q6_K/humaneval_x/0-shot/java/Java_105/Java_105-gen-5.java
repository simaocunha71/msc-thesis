Here is a Java solution:

```java
import java.util.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<String> result = new ArrayList<>();
        List<Integer> sorted = new ArrayList<>();

        // filter out numbers outside the range 1-9
        for (int num : arr) {
            if (num >= 1 && num <= 9) {
                sorted.add(num);
            }
        }

        // sort the filtered numbers
        Collections.sort(sorted);

        // reverse the sorted list
        Collections.reverse(sorted);

        // replace each digit by its corresponding name
        for (int num : sorted) {
            result.add(getName(num));
        }

        return result;
    }

    // helper function to get the name of a number
    private String getName(int num) {
        String[] names = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        return names[num];
    }
}
```

This solution first filters out numbers outside the range 1-9, then sorts the filtered numbers, reverses the sorted list, and finally replaces each digit by its corresponding name. If the array is empty, it returns an empty array. If the array has any strange numbers, it ignores them. The helper function `getName` returns the name of a number.  This solution assumes that the input array contains only integers and that the numbers in the range 1-9 are not repeated. If there are repeated numbers in the range 1-9, this solution will return the same name for each occurrence of the same number.  If there are numbers outside the range 1-9, this solution will ignore them and return an array containing the names of the numbers in the range 1-9.  If the array is null, this solution will return a null pointer exception.  If the array is not a list of integers, this solution will throw a class cast exception.  If the array contains non-integer objects, this solution will throw a class cast exception.  If the array contains numbers outside the range 1-9 and there are repeated numbers in the range 1-9, this solution will return the same name for each occurrence of the same number and ignore the numbers outside the range 1-9.  If the array contains numbers outside the range 1-9 and there are no repeated numbers in the range 1-9, this