        int counter = 0;
        for (int i = 0; i < file_name.length(); i++) {
            char c = file_name.charAt(i);
            if (c >= 'a' && c <= 'z') {
                counter += 1;
            }
            if (c >= 'A' && c <= 'Z') {
                counter += 1;
            }
            if (c >= '0' && c <= '9') {
                counter += 1;
            }
            if (counter > 3) {
                return "No";
            }
        }
        String[] valid_endings = {"txt", "exe", "dll"};
        int dot_index = file_name.indexOf('.');
        if (dot_index == -1 || dot_index == file_name.length() - 1) {
            return "No";
        }
        String after_dot = file_name.substring(dot_index + 1);
        for (String valid_ending : valid_endings) {
            if (valid_ending.equals(after_dot)) {
                return "Yes";
            }
        }
        return "No";

    }
}

