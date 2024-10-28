    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> result = new ArrayList<>();
        for (Double gpa : grades) {
            if (gpa >= 4.0) {
                result.add("A+");
            } else if (gpa > 3.7) {
                result.add("A");
            } else if (gpa > 3.3) {
                result.add("A-");
            } else if (gpa > 3.0) {
                result.add("B+");
            } else if (gpa > 2.7) {
                result.add("B");
            } else if (gpa > 2.3) {
                result.add("B-");
            } else if (gpa > 2.0) {
                result.add("C+");
            } else if (gpa > 1.7) {
                result.add("C");
            } else if (gpa > 1.3) {
                result.add("C-");
            } else if (gpa > 1.0) {
                result.add("D+");
            } else if (gpa > 0.7) {
                result.add("D");
            } else if (gpa > 0.0) {
                result.add("D-");
            } else {
                result.add("E");
            }
        }
        return result;
    } // End of method
} // End of class
// Example usage
List<Double> grades = Arrays.asList(4.0, 3.0, 1.7, 2.0, 3.5);
List<String> result = new Solution().numericalLetterGrade(grades);
System.out.println(result); // prints [A+, B, C-, C, A-]  // Example output
// Example usage
List<Double> grades2 = Arrays.asList(4.0, 3.5, 1.7, 2.0, 3.8);
List<String> result2 = new Solution().numericalLetterGrade(grades2);
System.out.println(result2); // prints [A+, A-, C, C, A]
// Example usage
List<Double> grades3 = Arrays.asList(1.0, 1.2, 1.3, 1.5, 1.9);
List<String> result3 = new Solution().numericalLetterGrade(grades3);
System.out.println(result