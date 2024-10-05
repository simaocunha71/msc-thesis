```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        // create a new list to store the result
        List<Integer> result = new ArrayList<>();
        // create a new list to store the sorted list
        List<Integer> sortedList = new ArrayList<>(lst);
        // sort the list in ascending order
        Collections.sort(sortedList);
        // create a new list to store the remaining integers
        List<Integer> remainingIntegers = new ArrayList<>(lst);
        // create a boolean to indicate whether to get the minimum or maximum value
        boolean getMin = true;
        // while there are remaining integers
        while (!remainingIntegers.isEmpty()) {
            // if getMin is true, get the minimum value from the remaining integers
            if (getMin) {
                int min = Collections.min(remainingIntegers);
                // add the minimum value to the result list
                result.add(min);
                // remove the minimum value from the remaining integers list
                remainingIntegers.remove(Integer.valueOf(min));
            } else {
                // if getMin is false, get the maximum value from the remaining integers
                int max = Collections.max(remainingIntegers);
                // add the maximum value to the result list
                result.add(max);
                // remove the maximum value from the remaining integers list
                remainingIntegers.remove(Integer.valueOf(max));
            }
            // toggle the getMin boolean
            getMin = !getMin;
        }
        // return the result list
        return result;
    }
}
```