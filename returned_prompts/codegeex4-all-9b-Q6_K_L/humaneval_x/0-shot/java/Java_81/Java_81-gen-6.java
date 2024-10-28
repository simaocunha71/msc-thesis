```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> gradesMap = new ArrayList<>();
        for (Double grade : grades) {
            if (grade == 4.0) {
                gradesMap.add("A+");
            } else if (grade > 3.7) {
                gradesMap.add("A");
            } else if (grade > 3.3) {
                gradesMap.add("A-");
            } else if (grade > 3.0) {
                gradesMap.add("B+");
            } else if (grade > 2.7) {
                gradesMap.add("B");
            } else if (grade > 2.3) {
                gradesMap.add("B-");
            } else if (grade > 2.0) {
                gradesMap.add("C+");
            } else if (grade > 1.7) {
                gradesMap.add("C");
            } else if (grade > 1.3) {
                gradesMap.add("C-");
            } else if (grade > 1.0) {
                gradesMap.add("D+");
            } else if (grade > 0.7) {
                gradesMap.add("D");
            } else if (grade > 0.0) {
                gradesMap.add("D-");
            } else {
                gradesMap.add("E");
            }
        }
        return gradesMap;
    }
}
```