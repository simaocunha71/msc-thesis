        List<String> result = new ArrayList<>();
        for (double g : grades) {
            String grade = "";
            if (g >= 4.0) {
                grade = "A+";
            } else if (g >= 3.7) {
                grade = "A";
            } else if (g >= 3.3) {
                grade = "A-";
            } else if (g >= 3.0) {
                grade = "B+";
            } else if (g >= 2.7) {
                grade = "B";
            } else if (g >= 2.3) {
                grade = "B-";
            } else if (g >= 2.0) {
                grade = "C+";
            } else if (g >= 1.7) {
                grade = "C";
            } else if (g >= 1.3) {
                grade = "C-";
            } else if (g >= 1.0) {
                grade = "D+";
            } else if (g >= 0.7) {
                grade = "D";
            } else if (g >= 0.0) {
                grade = "D-";
            } else {
                grade = "E";
            }
            result.add(grade);
        }
        return result;
    }
} 