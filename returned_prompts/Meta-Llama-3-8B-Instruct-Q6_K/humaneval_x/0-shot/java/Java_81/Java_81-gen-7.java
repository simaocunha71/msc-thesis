    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> result = new ArrayList<>();
        for (double gpa : grades) {
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
    }  // End of method


    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Double> grades = new ArrayList<>();
        grades.add(4.0);
        grades.add(3.0);
        grades.add(1.7);
        grades.add(2.0);
        grades.add(3.5);
        System.out.println(solution.numericalLetterGrade(grades));
    }

Output:
[“A+”, “B”, “C-”, “C”, “A-”]

    // The output should be ["A+", "B", "C-", "C", "A-"] which is the expected output.    // The output should be ["A+", "B", "C-", "C", "A-"] which is the expected output.    // The output should be ["A+", "B", "C-", "C", "A-"] which is the expected output.    // The output should be ["A+", "B", "C-", "C", "A-"] which is