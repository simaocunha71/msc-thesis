        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if(i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }
}


A: Here is the corrected Java code:

```java
import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if(i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> numbers = Arrays.asList(1, 2, 3);
        int delimiter = 4;
        System.out.println(solution.intersperse(numbers, delimiter));
    }
}
```

This code creates a new list and adds each element of the input list to the new list followed by the delimiter. If it is the last element in the list, it does not add the delimiter after it.

In the `main` method, we create a `Solution` object and a list of numbers. We then call the `intersperse` method with the list of numbers and the delimiter, and print the result.

When you run this code, it will print:

```
[1, 4, 2, 4, 3]
```

This is the expected output as per the problem statement.



I hope this helps. If you have any questions, feel free to ask.





































