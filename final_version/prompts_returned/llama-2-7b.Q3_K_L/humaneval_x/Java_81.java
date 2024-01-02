import java.util.*;
import java.lang.*;

class Solution {
    /**
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A
            > 3.3                A-
            > 3.0                B+
            > 2.7                B
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+
            > 0.7                D
            > 0.0                D-
              0.0                E


    Example:
    numericalLetterGrade(Arrays.asList(4.0, 3, 1.7, 2, 3.5)) ==> ["A+", "B", "C-", "C", "A-"]
     */
    public List<String> numericalLetterGrade(List<Double> grades) {
        // Your code here
        if (grades == null || grades.size() <= 1)
            return new ArrayList<>();
        
        Map map = new HashMap();
        for(int i=0;i<4;i++){
            double[] c = new double[2];
            c[0] = (i+1);//min value
            c[1]=c[0]+1.0;//max value
             map.put(""+(i+1), ""+(i+1)+":"+"C");
        }
        
        Collections.sort(grades);
        
        List<String> list = new ArrayList<>();
        for (int i = 0; i < grades.size(); i++) {
            double gpa = grades.get(i);
            
            if