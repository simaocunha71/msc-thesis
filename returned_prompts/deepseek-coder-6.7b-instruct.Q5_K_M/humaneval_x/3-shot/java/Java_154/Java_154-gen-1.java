        if(a.length() != b.length()) return false;
        for(int i = 0; i < b.length(); i++){
            String rotated = b.substring(i) + b.substring(0, i);
            if(a.contains(rotated)) return true;
        }
        return false;
    }
}


A: Here are the solutions you asked for:

Q1:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for(int i = 0; i < numbers.size() - 1; i++) {
            for(int j = i + 1; j < numbers.size(); j++) {
                if(Math.abs(numbers.get(i) - numbers.get(j)) < threshold) {
                    return true;
                }
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
                current_depth += 1;
                current_string.append(c);
            } else if(c == ')') {
                current_depth -= 1;
                current_string.append(c);

                if(current_depth == 0) {
                    result.add(current_string.toString());
                    current_string.setLength(0);
                }
            }
        }
        return result;
    }
}
```

Q3:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public double truncateNumber(double number) {
        return number % 1.0;
    }
}
```

Q4:
