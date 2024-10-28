        int count = 0;
        for  (char c : brackets.toCharArray()) {
            if  (c == '<') {
                count += 1;
            } else if  (c == '>') {
                count -= 1;
                if  (count < 0) {
                    return false;
                }
            }
        }
        return count == 0;
     }
}


A: Here are the solutions with comments to explain the logic used:

Q1:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        // Loop through each pair of numbers in the list
        for(int i = 0; i < numbers.size() - 1; i++) {
            for(int j = i + 1; j < numbers.size(); j++) {
                // If the absolute difference between the two numbers is less than the threshold, return true
                if(Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                    return true;
                }
            }
        }
        // If no pair of numbers had a difference less than the threshold, return false
        return false;
    }
}
```

Q2:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        // Initialize list for results and current string for building groups
        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        // Initialize count of parentheses depth
        int current_depth = 0;

        // Loop through each character in the string
        for(char c : paren_string.toCharArray()) {
            // If character is an opening parenthesis, increase depth and add to current string
            if(c == '(') {
                current_depth += 1;
                current_string.append(c);
            }
            // If character is a closing parenthesis, decrease depth and add to current string
            else if(c == '