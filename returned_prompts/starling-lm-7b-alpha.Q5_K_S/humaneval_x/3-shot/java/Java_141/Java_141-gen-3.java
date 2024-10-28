        String[] valid_extensions = {"txt", "exe", "dll"};
        String[] invalid_digits = "0123456789".toCharArray();
        String[] invalid_chars = "0123456789".toCharArray();
        int count_digits = 0;
        boolean has_dot = false;
        boolean has_chars = false;
        for (char c : file_name.toCharArray()) {
            if (Arrays.asList(invalid_digits).contains(c)) {
                count_digits += 1;
            }
            if (c == '.') {
                has_dot = true;
            }
            if (Character.isLetter(c)) {
                has_chars = true;
            }
        }
        if (count_digits > 3) return "No";
        if (!has_dot) return "No";
        if (!has_chars) return "No";
        for (String ext : valid_extensions) {
            if (file_name.endsWith("." + ext)) return "Yes";
        }
        return "No";
    }
}



```