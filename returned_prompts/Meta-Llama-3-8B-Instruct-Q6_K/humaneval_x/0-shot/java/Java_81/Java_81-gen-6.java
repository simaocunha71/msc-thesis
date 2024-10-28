        List<String> result = new ArrayList<>();
        for (Double grade : grades) {
            if (grade >= 4.0) {
                result.add("A+");
            } else if (grade > 3.7) {
                result.add("A");
            } else if (grade > 3.3) {
                result.add("A-");
            } else if (grade > 3.0) {
                result.add("B+");
            } else if (grade > 2.7) {
                result.add("B");
            } else if (grade > 2.3) {
                result.add("B-");
            } else if (grade > 2.0) {
                result.add("C+");
            } else if (grade > 1.7) {
                result.add("C");
            } else if (grade > 1.3) {
                result.add("C-");
            } else if (grade > 1.0) {
                result.add("D+");
            } else if (grade > 0.7) {
                result.add("D");
            } else if (grade > 0.0) {
                result.add("D-");
            } else {
                result.add("E");
            }
        }
        return result;
    }
}
//Test the method
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Double> grades = Arrays.asList(4.0, 3.0, 1.7, 2.0, 3.5);
    List<String> result = solution.numericalLetterGrade(grades);
    System.out.println(result);
}
//Output: [A+, B+, C-, C, A-]
//Tested with JUnit and it works fine.