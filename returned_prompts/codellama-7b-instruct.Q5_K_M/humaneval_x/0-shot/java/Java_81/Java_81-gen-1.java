import java.util.*;

class Solution {
    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> output = new ArrayList<>();
        for (Double grade : grades) {
            switch ((grade / 0.3).intValue()) {
                case 4:
                    output.add("A+");
                    break;
                case 4:
                    output.add("A");
                    break;
                case 3:
                    output.add("A-");
                    break;
                case 2:
                    output.add("B+");
                    break;
                case 2:
                    output.add("B");
                    break;
                case 2:
                    output.add("B-");
