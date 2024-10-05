        if(array.size() == 0) return array;
        int sum = array.get(0) + array.get(array.size()-1);
        boolean isOdd = sum % 2 != 0;
        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);
        if(isOdd) return sortedArray;
        else{
            Collections.reverse(sortedArray);
            return sortedArray;
        }
    }
}

I have no idea about this task. I can't understand the task and how to solve it. Please help me to understand this.

A: The task is to sort the given array, but with a twist. If the sum of the first and last elements in the array is odd, the array should be sorted in ascending order. If the sum is even, it should be sorted in descending order.

So, for example, with the array [2, 4, 3, 0, 1, 5], the sum of the first (2) and last (5) elements (2 + 5 = 7) is odd, so you would sort the array in ascending order. The result would be [0, 1, 2, 3, 4, 5].

And for the array [2, 4, 3, 0, 1, 5, 6], the sum of the first (2) and last (6) elements (2 + 6 = 8) is even, so you would sort the array in descending order. The result would be [6, 5, 4, 3, 2, 1, 0].

Here is the Java code that accomplishes this:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array.size() == 0) return array;

        int sum = array.get(0) + array.get(array.size()-1);
        boolean isOdd = sum % 2 != 0;

        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        return