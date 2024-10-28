```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> letters = new ArrayList<>();
        for (Double grade : grades) {
            if (grade == 4.0) {
                letters.add("A+");
            } else if (grade > 3.7) {
                letters.add("A");
            } else if (grade > 3.3) {
                letters.add("A-");
            } else if (grade > 3.0) {
                letters.add("B+");
            } else if (grade > 2.7) {
                letters.add("B");
            } else if (grade > 2.3) {
                letters.add("B-");
            } else if (grade > 2.0) {
                letters.add("C+");
            } else if (grade > 1.7) {
                letters.add("C");
            } else if (grade > 1.3) {
                letters.add("C-");
            } else if (grade > 1.0) {
                letters.add("D+");
            } else if (grade > 0.7) {
                letters.add("D");
            } else if (grade > 0.0) {
                letters.add("D-");
            } else {
                letters.add("E");
            }
        }
        return letters;
    }
}
```
