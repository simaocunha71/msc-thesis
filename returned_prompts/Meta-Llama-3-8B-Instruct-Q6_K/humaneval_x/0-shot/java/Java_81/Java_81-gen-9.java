    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> result = new ArrayList<>();
        for (double grade : grades) {
            String letterGrade = "";
            if (grade >= 4.0) {
                letterGrade = "A+";
            } else if (grade > 3.7) {
                letterGrade = "A";
            } else if (grade > 3.3) {
                letterGrade = "A-";
            } else if (grade > 3.0) {
                letterGrade = "B+";
            } else if (grade > 2.7) {
                letterGrade = "B";
            } else if (grade > 2.3) {
                letterGrade = "B-";
            } else if (grade > 2.0) {
                letterGrade = "C+";
            } else if (grade > 1.7) {
                letterGrade = "C";
            } else if (grade > 1.3) {
                letterGrade = "C-";
            } else if (grade > 1.0) {
                letterGrade = "D+";
            } else if (grade > 0.7) {
                letterGrade = "D";
            } else if (grade > 0.0) {
                letterGrade = "D-";
            } else {
                letterGrade = "E";
            }
            result.add(letterGrade);
        }
        return result;
    }
}  // This is the correct solution. It iterates over each grade in the list, and based on the grade, it assigns a letter grade and adds it to the result list. The result list is then returned.  // The time complexity of this solution is O(n), where n is the number of grades.  // The space complexity is also O(n), as we are storing the result in a list.  // This solution is efficient and easy to understand.  // It can be improved by using a switch statement instead of if-else chain, but it won't change the time complexity.  // This solution is also easy to extend, if the grading system is changed in the future.  // It is also easy to test and debug.  // This solution is a good example of how to solve a problem using a clear and concise code.  // It is a good example of how to use a loop to iterate over a collection and how to use an if-else