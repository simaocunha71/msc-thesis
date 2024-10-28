        if (file_name.length() > 3) {
            return "No";
        }
        int dot = file_name.indexOf(".");
        if (dot == -1) {
            return "No";
        }
        if (dot != file_name.length() - 1) {
            return "No";
        }
        String before_dot = file_name.substring(0, dot);
        if (before_dot.length() == 0) {
            return "No";
        }
        if (before_dot.chars().filter(ch -> Character.isDigit(ch)).count() > 3) {
            return "No";
        }
        if (before_dot.chars().filter(ch -> Character.isLetter(ch)).count() == 0) {
            return "No";
        }
        String after_dot = file_name.substring(dot + 1);
        if (after_dot.length() == 0) {
            return "No";
        }
        if (after_dot.equals("txt") || after_dot.equals("exe") || after_dot.equals("dll")) {
            return "Yes";
        }
        return "No";
    }
}



























































































































































































































