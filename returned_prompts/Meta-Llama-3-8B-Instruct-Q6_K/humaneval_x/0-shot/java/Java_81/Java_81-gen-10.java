    public List<String> numericalLetterGrade(List<Double> grades) {
        List<String> letterGrades = new ArrayList<>();
        for (double gpa : grades) {
            String letterGrade = "";
            if (gpa >= 4.0) {
                letterGrade = "A+";
            } else if (gpa > 3.7) {
                letterGrade = "A";
            } else if (gpa > 3.3) {
                letterGrade = "A-";
            } else if (gpa > 3.0) {
                letterGrade = "B+";
            } else if (gpa > 2.7) {
                letterGrade = "B";
            } else if (gpa > 2.3) {
                letterGrade = "B-";
            } else if (gpa > 2.0) {
                letterGrade = "C+";
            } else if (gpa > 1.7) {
                letterGrade = "C";
            } else if (gpa > 1.3) {
                letterGrade = "C-";
            } else if (gpa > 1.0) {
                letterGrade = "D+";
            } else if (gpa > 0.7) {
                letterGrade = "D";
            } else if (gpa > 0.0) {
                letterGrade = "D-";
            } else {
                letterGrade = "E";
            }
            letterGrades.add(letterGrade);
        }
        return letterGrades;
    }
}