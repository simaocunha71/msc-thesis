```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        Map<Double, String> letterGrades = new HashMap<>();
        letterGrades.put(4.0, "A+");
        letterGrades.put(3.7, "A");
        letterGrades.put(3.3, "A-");
        letterGrades.put(3.0, "B+");
        letterGrades.put(2.7, "B");
        letterGrades.put(2.3, "B-");
        letterGrades.put(2.0, "C+");
        letterGrades.put(1.7, "C");
        letterGrades.put(1.3, "C-");
        letterGrades.put(1.0, "D+");
        letterGrades.put(0.7, "D");
        letterGrades.put(0.0, "D-");
        letterGrades.put(0.0, "E");

        List<String> result = new ArrayList<>();
        for (Double grade : grades) {
            if (letterGrades.containsKey(grade)) {
                result.add(letterGrades.get(grade));
            }
        }
        return result;
    }
}
```