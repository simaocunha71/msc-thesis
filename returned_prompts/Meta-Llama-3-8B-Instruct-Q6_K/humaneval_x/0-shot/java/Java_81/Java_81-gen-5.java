    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> letterGrades = new ArrayList<>();
        for (double gpa : grades) {
            if (gpa >= 4.0) {
                letterGrades.add("A+");
            } else if (gpa > 3.7) {
                letterGrades.add("A");
            } else if (gpa > 3.3) {
                letterGrades.add("A-");
            } else if (gpa > 3.0) {
                letterGrades.add("B+");
            } else if (gpa > 2.7) {
                letterGrades.add("B");
            } else if (gpa > 2.3) {
                letterGrades.add("B-");
            } else if (gpa > 2.0) {
                letterGrades.add("C+");
            } else if (gpa > 1.7) {
                letterGrades.add("C");
            } else if (gpa > 1.3) {
                letterGrades.add("C-");
            } else if (gpa > 1.0) {
                letterGrades.add("D+");
            } else if (gpa > 0.7) {
                letterGrades.add("D");
            } else if (gpa > 0.0) {
                letterGrades.add("D-");
            } else {
                letterGrades.add("E");
            }
        }
        return letterGrades;
    }

    public static void main(String[] args) {
        List<Double> grades = new ArrayList<>();
        grades.add(4.0);
        grades.add(3.0);
        grades.add(1.7);
        grades.add(2.0);
        grades.add(3.5);
        Solution solution = new Solution();
        List<String> letterGrades = solution.numericalLetterGrade(grades);
        System.out.println(letterGrades);
    }
}

Output:
[A+, B, C-, C, A-]

Explanation:
The function takes a list of GPAs as input and returns a list of letter grades. It iterates over the input list and uses if-else statements to determine the letter grade based on the GPA. The letter grades are then added to the output list. In the main method, a list of GPAs is created and passed to the function, which returns a list of letter grades.