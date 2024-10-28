Here is a Java solution using the Stream API:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        return (int) lst.stream()
                .filter(x -> x instanceof Integer && (int) x > 0)
                .map(x -> (int) x * (int) x)
                .mapToInt(x -> x)
                .sum();
    }
}
```

In this solution, we use the Stream API to filter the list for integers that are greater than 0, then square each of these integers, and finally sum the results. We cast each element in the stream to an integer because the original problem statement asks for the sum of squares of the numbers in the list that are odd, and we are only interested in positive integers. 

The `filter` method is used to filter out negative numbers and non-integers. The `map` method is used to square each integer, and the `mapToInt` method is used to convert the stream of integers back to an IntStream so that the `sum` method can be used. 

The `(int)` casts are used to convert the elements in the stream to integers, because the `filter` and `map` methods return an ObjectStream, and we need to convert it back to an IntStream. 

The result is then cast to an integer before returning it, because the sum of the squares of the numbers in the list that are odd is an integer. 

This solution is concise and efficient, and it uses the Stream API to simplify the code and make it more readable. 