```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> res = new ArrayList<>();
        for (Double g : grades) {
            if (g == 4.0) {
                res.add("A+");
            } else if (g > 3.7) {
                res.add("A");
            } else if (g > 3.3) {
                res.add("A-");
            } else if (g > 3.0) {
                res.add("B+");
            } else if (g > 2.7) {
                res.add("B");
            } else if (g > 2.3) {
                res.add("B-");
            } else if (g > 2.0) {
                res.add("C+");
            } else if (g > 1.7) {
                res.add("C");
            } else if (g > 1.3) {
                res.add("C-");
            } else if (g > 1.0) {
                res.add("D+");
            } else if (g > 0.7) {
                res.add("D");
            } else if (g > 0.0) {
                res.add("D-");
            } else {
                res.add("E");
            }
        }
        return res;
    }
}
```