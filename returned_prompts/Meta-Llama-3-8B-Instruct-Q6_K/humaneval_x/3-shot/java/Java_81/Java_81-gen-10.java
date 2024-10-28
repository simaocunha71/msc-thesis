        List<String> result = new ArrayList<>();
        for (double g : grades) {
            String letter_grade = "";
            if (g > 4.0) {
                letter_grade = "A+";
            } else if (g > 3.7) {
                letter_grade = "A";
            } else if (g > 3.3) {
                letter_grade = "A-";
            } else if (g > 3.0) {
                letter_grade = "B+";
            } else if (g > 2.7) {
                letter_grade = "B";
            } else if (g > 2.3) {
                letter_grade = "B-";
            } else if (g > 2.0) {
                letter_grade = "C+";
            } else if (g > 1.7) {
                letter_grade = "C";
            } else if (g > 1.3) {
                letter_grade = "C-";
            } else if (g > 1.0) {
                letter_grade = "D+";
            } else if (g > 0.7) {
                letter_grade = "D";
            } else if (g > 0.0) {
                letter_grade = "D-";
            } else {
                letter_grade = "E";
            }
            result.add(letter_grade);
        }
        return result;
    }
}