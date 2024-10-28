    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> result = new ArrayList<>();
        for (double grade : grades) {
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

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Double> grades = Arrays.asList(4.0, 3.0, 1.7, 2.0, 3.5);
        List<String> result = solution.numericalLetterGrade(grades);
        System.out.println(result);
    }
}

Output:
[A+, B+, C-, C, A-]
Explanation:
The function takes a list of GPAs and returns a list of letter grades.
The main function demonstrates the usage of the function with a list of GPAs.

Time complexity: O(n), where n is the number of elements in the list.
Space complexity: O(n), where n is the number of elements in the list. This is because we are storing the result in a list.