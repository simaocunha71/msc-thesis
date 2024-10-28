Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] fruits = s.split(" ");
        int appleCount = 0;
        int orangeCount = 0;
        for (String fruit : fruits) {
            if (fruit.contains("apples")) {
                appleCount = Integer.parseInt(fruit.replace("apples", "").trim());
            } else if (fruit.contains("oranges")) {
                orangeCount = Integer.parseInt(fruit.replace("oranges", "").trim());
            }
        }
        return n - appleCount - orangeCount;
    }
}
```

This solution works by splitting the input string into an array of strings, where each string represents a fruit type and its count. It then iterates over this array to find the counts of apples and oranges. Finally, it returns the total number of fruits minus the counts of apples and oranges. This will give the number of mango fruits in the basket.

For example, if the input string is "5 apples and 6 oranges", the solution will parse it as follows:
- "apples" contains "apples", so appleCount will be set to 5.
- "oranges" contains "oranges", so orangeCount will be set to 6.
Then, it will return n - appleCount - orangeCount, which is 19 - 5 - 6 = 8. This means there are 8 mango fruits in the basket.