        List<String> letterGrades = new ArrayList<>();

        for(Double grade : grades){
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

This code will take a list of GPA scores and return a list of corresponding letter grades. It checks each GPA in the provided list, and adds the appropriate letter grade to the new list. If the GPA is less than 0.0, the letter grade 'E' is added to the list.
*/


A: Here is a more efficient way to solve this problem. It uses a switch-case block to map the GPAs to their respective letter grades. 

```java
import java.util.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> letterGrades = new ArrayList<>();

        for (Double grade : grades) {
            switch (grade.intValue()) {