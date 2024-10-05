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
}  