        List<String> result = new ArrayList<>();
        for (double gpa : grades) {
            if (gpa > 4.0) gpa = 4.0;
            if (gpa < 0.0) gpa = 0.0;
            String letter_grade;
            if (gpa > 3.7) {
                letter_grade = "A";
                if (gpa > 3.7) letter_grade += "+";
                if (gpa > 3.3) letter_grade += "-";
            } else {
                letter_grade = "" + (char) (gpa + 65);
            }
            result.add(letter_grade);
        }
        return result;
    }
}

