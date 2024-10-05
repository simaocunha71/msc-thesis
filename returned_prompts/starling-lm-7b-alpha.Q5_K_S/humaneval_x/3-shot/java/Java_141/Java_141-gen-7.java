        String[] valid_extensions = { "txt", "exe", "dll" };
        String[] invalid_characters = { " ", ".", "$", "@", "#", "*" };
        int length = file_name.length();
        boolean valid = true;
        int digits = 0;
        for (char c : file_name.toCharArray()) {
            if (Character.isDigit(c)) {
                digits += 1;
            }
        }
        if (length < 3 || length > 255 || digits > 3 || file_name.contains("..") || !file_name.contains(".") || !Character.isLetter(file_name.charAt(0))) {
            valid = false;
        }
        for (String extension : valid_extensions) {
            if (file_name.endsWith(extension)) {
                for (char c : file_name.toCharArray()) {
                    if (Arrays.asList(invalid_characters).contains(String.valueOf(c))) {
                        valid = false;
                    }
                }
            }
        }
        return valid ? "Yes" : "No";
    }
}

