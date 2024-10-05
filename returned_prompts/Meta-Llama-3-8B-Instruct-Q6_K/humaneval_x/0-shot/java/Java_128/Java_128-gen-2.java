Here is the solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if(arr.isEmpty()) {
            return Optional.empty();
        }
        int sign = 1;
        int sum = 0;
        for(int num : arr) {
            if(num == 0) {
                return Optional.empty();
            }
            sign *= (num > 0) ? 1 : -1;
            sum += Math.abs(num);
        }
        return Optional.of(sign * sum);
    }
}
```

Explanation: 

The solution first checks if the array is empty. If it is, it returns an empty optional. Then, it initializes two variables: `sign` to keep track of the product of signs and `sum` to keep track of the sum of magnitudes. It iterates over the array, updating `sign` based on the sign of each number and updating `sum` by adding the absolute value of each number to it. If it encounters a zero in the array, it returns an empty optional, as per the problem statement. Finally, it returns an optional containing the product of `sign` and `sum`. 

Note: In Java, `Optional` is a container that may or may not contain a non-null value. It is used to represent the possibility of a missing value. In this case, we are using it to represent the possibility of an empty array. If the array is empty, the `Optional` will be empty; otherwise, it will contain the result. 

This solution has a time complexity of O(n), where n is the number of elements in the array, as it iterates over the array once. The space complexity is O(1), as it uses a constant amount of space to store the variables. 