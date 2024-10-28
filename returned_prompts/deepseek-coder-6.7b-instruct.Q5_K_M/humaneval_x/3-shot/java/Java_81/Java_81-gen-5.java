        List<String> letterGrades = new ArrayList<String>();
        for (double grade : grades) {
            if (grade == 4.0) {
                letterGrades.add("A+");
            } else if (grade > 3.7) {
                letterGrades.add("A");
            } else if (grade > 3.3) {
                letterGrades.add("A-");
            } else if (grade > 3.0) {
                letterGrades.add("B+");
            } else if (grade > 2.7) {
                letterGrades.add("B");
            } else if (grade > 2.3) {
                letterGrades.add("B-");
            } else if (grade > 2.0) {
                letterGrades.add("C+");
            } else if (grade > 1.7) {
                letterGrades.add("C");
            } else if (grade > 1.3) {
                letterGrades.add("C-");
            } else if (grade > 1.0) {
                letterGrades.add("D+");
            } else if (grade > 0.7) {
                letterGrades.add("D");
            } else if (grade > 0.0) {
                letterGrades.add("D-");
            } else {
                letterGrades.add("E");
            }
        }
        return letterGrades;
     }
}


A: Here is the solution for your problems:

Problem 1:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean hasCloseElements(List<Double> numbers, double threshold) {
        for(int i = 0; i < numbers.size()-1; i++) {
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

Problem 2:

```java
import java.util.*;
