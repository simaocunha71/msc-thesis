The problem can be solved by parsing the input string to extract the number of apples and oranges, and then subtracting those numbers from the total number of fruits.

Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] parts = s.split(" ");
        String[] fruits = parts[parts.length - 1].split("and");
        int apples = 0;
        int oranges = 0;
        for (String fruit : fruits) {
            if (fruit.contains("apples")) {
                apples = Integer.parseInt(fruit.replace("apples", ""));
            } else if (fruit.contains("oranges")) {
                oranges = Integer.parseInt(fruit.replace("oranges", ""));
            }
        }
        return n - apples - oranges;
    }
}
```

In this solution, we first split the input string into parts using the space character as a delimiter. Then, we split the last part (which contains the fruits) into individual fruits using the "and" keyword as a delimiter.

We then iterate over the fruits and check if each fruit contains the word "apples" or "oranges". If it does, we parse the fruit to extract the number of fruits and update the corresponding variable.

Finally, we return the total number of fruits minus the number of apples and oranges. This gives us the number of mango fruits in the basket.