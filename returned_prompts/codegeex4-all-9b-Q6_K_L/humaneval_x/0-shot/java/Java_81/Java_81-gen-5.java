```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> out = new ArrayList<>();
        for (Double grade : grades) {
            if (grade == 4.0) {
                out.add("A+");
            } else if (grade > 3.7) {
                out.add("A");
            } else if (grade > 3.3) {
                out.add("A-");
            } else if (grade > 3.0) {
                out.add("B+");
            } else if (grade > 2.7) {
                out.add("B");
            } else if (grade > 2.3) {
                out.add("B-");
            } else if (grade > 2.0) {
                out.add("C+");
            } else if (grade > 1.7) {
                out.add("C");
            } else if (grade > 1.3) {
                out.add("C-");
            } else if (grade > 1.0) {
                out.add("D+");
            } else if (grade > 0.7) {
                out.add("D");
            } else if (grade > 0.0) {
                out.add("D-");
            } else {
                out.add("E");
            }
        }
        return out;
    }
}
```

This solution iterates through the list of grades and checks the condition for each grade. If the grade matches the condition, it adds the corresponding letter grade to the output list. If none of the conditions match, it adds "E" to the output list.