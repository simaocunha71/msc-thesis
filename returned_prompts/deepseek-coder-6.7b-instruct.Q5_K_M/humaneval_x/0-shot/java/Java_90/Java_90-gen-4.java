        if(lst == null || lst.size() < 2){
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for(Integer num : lst){
            if(num < smallest){
                secondSmallest = smallest;
                smallest = num;
            } else if(num > smallest && num < secondSmallest){
                secondSmallest = num;
            }
        }

        if(secondSmallest == Integer.MAX_VALUE){
            return Optional.empty();
        }

        return Optional.of(secondSmallest);
    }
}

```



## Answer 2
```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if(lst == null || lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for(Integer num : lst) {
            if(num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            } else if(num > smallest && num < secondSmallest) {
                secondSmallest = num;
            }
        }

        if(secondSmallest == Integer.MAX_VALUE) {
            return Optional.empty();
        }

        return Optional.of(secondSmallest);
    }
}
```



## Answer 3
```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if(lst == null || lst.size() < 2) {
            return Optional.empty();
        }

        int smallest = Integer.MAX_VALUE;
        int secondSmallest = Integer.MAX_VALUE;

        for(Integer num : lst) {
            if(num < smallest) {
                secondSmallest = smallest;
                smallest = num;
            }