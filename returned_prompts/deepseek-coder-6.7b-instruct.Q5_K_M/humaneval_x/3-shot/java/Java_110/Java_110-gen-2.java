        int oddCount1 = 0;
        int oddCount2 = 0;

        for(int i = 0; i < lst1.size(); i++) {
            if(lst1.get(i) % 2 != 0) {
                oddCount1++;
            }
        }

        for(int i = 0; i < lst2.size(); i++) {
            if(lst2.get(i) % 2 != 0) {
                oddCount2++;
            }
        }

        if(oddCount1 == 0 || oddCount2 == 0) {
            return "YES";
        }

        if(oddCount1 > oddCount2) {
            return "NO";
        }

        return "YES";

     }
}


A: Here are the solutions:
Q1:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for(int i = 0; i < numbers.size()-1; i++) {
            for(int j = i+1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if(distance < threshold) return true;
            }
        }
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
        List<String> result = new ArrayList<>();
        StringBuilder current_string = new StringBuilder();
        int current_depth = 0;

        for(char c : paren_string.toCharArray()) {
            if(c == '(') {
                current_depth++;
                current_string.append(c);
            } else if(c == ')') {
                current_depth--;
                current_string.append(c);

                if(current_depth == 0) {
                    result.add(current_