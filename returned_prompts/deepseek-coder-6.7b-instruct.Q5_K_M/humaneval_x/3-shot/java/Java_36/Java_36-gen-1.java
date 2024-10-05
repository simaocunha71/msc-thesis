        int count = 0;
        for(int i = 11; i < n; i++) {
            if(i % 11 == 0 || i % 13 == 0) {
                count += countDigits(i);
            }
        }
        return count;
    }

    private int countDigits(int number) {
        int count = 0;
        while(number > 0) {
            if(number % 10 == 7) {
                count++;
            }
            number /= 10;
        }
        return count;
    }
}


A: Here is the corrected solution:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    >>> hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5)
    false
    >>> hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3)
    true
      */
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                double distance = Math.abs(numbers.get(i) - numbers.get(j));
                if (distance < threshold) return true;
            }
        }
        return false;
    }
}
```

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced  (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separateParenGroups("(  )  (( ))  (( )( 