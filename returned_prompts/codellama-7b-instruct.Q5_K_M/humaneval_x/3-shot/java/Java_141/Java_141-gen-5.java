        int digit_count = 0;
        char[] file_name_chars = file_name.toCharArray();
        for (char c : file_name_chars) {
            if (c >= '0' && c <= '9') {
                digit_count += 1;
            }
        }
        if (digit_count > 3) {
            return "No";
        }
        int dot_index = file_name.indexOf('.');
        if (dot_index == -1) {
            return "No";
        }
        if (dot_index == 0) {
            return "No";
        }
        if (dot_index == file_name.length() - 1) {
            return "No";
        }
        if (file_name.charAt(0) >= 'a' && file_name.charAt(0) <= 'z') {
            return "Yes";
        }
        if (file_name.charAt(0) >= 'A' && file_name.charAt(0) <= 'Z') {
            return "Yes";
        }
        return "No";
    }
}
