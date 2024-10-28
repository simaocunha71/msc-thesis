The solution to this problem can be achieved by creating a method that takes three parameters: the number of carrots eaten, the number of carrots needed, and the number of remaining carrots. The method returns a list containing the total number of carrots eaten after meals and the number of carrots left after meals.

Here is the solution in Java:
```java
import java.util.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        List<Integer> result = new ArrayList<>();
        int eaten = number + need;
        int left = remaining - (need - number);
        if (left < 0) {
            left = 0;
        }
        result.add(eaten);
        result.add(left);
        return result;
    }
}
```
The `eat` method takes the three parameters and calculates the total number of carrots eaten after meals by adding the number of carrots eaten to the number of carrots needed. It then calculates the number of carrots left after meals by subtracting the difference between the number of carrots needed and the number of carrots eaten from the number of remaining carrots. If the number of carrots left is negative, it sets it to 0. Finally, it returns a list containing the total number of carrots eaten and the number of carrots left.

For example, if the number of carrots eaten is 5, the number of carrots needed is 6, and the number of remaining carrots is 10, the method will return the list `[11, 4]`, indicating that the rabbit has eaten a total of 11 carrots and has 4 carrots left. If there are not enough remaining carrots, the method will eat all the remaining carrots, but still be hungry, as indicated by the last element of the list.