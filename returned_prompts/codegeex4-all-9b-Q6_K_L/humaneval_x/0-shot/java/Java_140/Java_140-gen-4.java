```java
import java.util.*;
import java.lang.*;

class Solution {
    public String fixSpaces(String text) {
        // First, replace all spaces with underscores
        String result = text.replaceAll(" ", "_");
        
        // Then, replace all consecutive underscores with a single underscore
        result = result.replaceAll("__+", "_");
        
        // Finally, replace all single underscores with a dash
        result = result.replaceAll("_", "-");
        
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        System.out.println(solution.fixSpaces("Example")); // "Example"
        System.out.println(solution.fixSpaces("Example 1")); // "Example_1"
        System.out.println(solution.fixSpaces(" Example 2")); // "_Example_2"
        System.out.println(solution.fixSpaces(" Example   3")); // "_Example-3"
    }
}
```