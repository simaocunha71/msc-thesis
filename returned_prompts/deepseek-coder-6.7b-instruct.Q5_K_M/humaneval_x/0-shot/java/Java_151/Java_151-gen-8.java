        int sum = 0;
        for(Object o: lst){
            if(o instanceof Integer){
                int num = (int) o;
                if(num < 0){
                    continue;
                }
                if(num % 2 != 0){
                    sum += num * num;
                }
            }
        }
        return sum;
    }
}





```



```java
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) == 1 
    doubleTheDifference(Arrays.asList(-1, -2, 0)) 
    doubleTheDifference(Arrays.asList(9, -2)) 
    doubleTheDifference(Arrays.asList(0)) 

    If the input list is empty, return 0.
      */
    public int doubleTheDifference(List<Object> lst)  {

        int sum = 0;
        for(Object o: lst){
            if(o instanceof Integer){
                int num = (int) o;
                if(num < 0){
                    continue;
                }
                if(num % 2 != 0){
                    sum += num * num;
                }
            }
        }
        return sum;
    }
}
```





```java
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.

    doubleTheDifference(Arrays.asList(1, 3, 2, 0)) 
    doubleTheDifference(Arrays.asList(-1, -2, 0)) 
    doubleTheDifference(Arrays.asList(9, -2)) 
    doubleTheDifference(Ar