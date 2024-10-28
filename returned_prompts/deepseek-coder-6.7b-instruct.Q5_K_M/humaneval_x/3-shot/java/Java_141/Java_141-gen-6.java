        int dot_index = file_name.lastIndexOf('.');
        if  (dot_index  != -1  &&  file_name.indexOf('.')  != dot_index)  return  "No";
        if  (dot_index  == -1)  return  "No";

        String base_name =  file_name.substring(0, dot_index);
        String extension =  file_name.substring(dot_index  +  1);

        if  (base_name.matches(".*\\d{4,}.*"))  return  "No";
        if  (!Character.isLetter(base_name.charAt(0)))  return  "No";
        if  (!["txt",  "exe",  "dll"].contains(extension))  return  "No";
        return  "Yes";
     }
}


A: There are some syntax errors in your code. Here's the corrected version:

Q1:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size() - 1; i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
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

        for (char c : paren_string.toCharArray()) {
            if (c == '(') {
                current_depth += 1;
                current_string.append(c);
            } else if (c == ')') {
                current_depth -= 