        int count = 0;
        int i = 0;
        while (i < file_name.length()) {
            if (file_name.charAt(i) >= '0' && file_name.charAt(i) <= '9') {
                count++;
            }
            i++;
        }
        if (count > 3) {
            return "No";
        }
        i = 0;
        int dot = 0;
        while (i < file_name.length()) {
            if (file_name.charAt(i) == '.') {
                dot++;
            }
            i++;
        }
        if (dot != 1) {
            return "No";
        }
        i = 0;
        while (i < file_name.length()) {
            if (file_name.charAt(i) != '.') {
                if (!(file_name.charAt(i) >= 'a' && file_name.charAt(i) <= 'z') && !(file_name.charAt(i) >= 'A' && file_name.charAt(i) <= 'Z')) {
                    return "No";
                }
            }
            i++;
        }
        i = file_name.length() - 1;
        while (i >= 0) {
            if (!(file_name.charAt(i) == '.' || (file_name.charAt(i) >= 'a' && file_name.charAt(i) <= 'z') || (file_name.charAt(i) >= 'A' && file_name.charAt(i) <= 'Z'))) {
                return "No";
            }
            i--;
        }

        if (!(file_name.endsWith("txt") || file_name.endsWith("exe") || file_name.endsWith("dll"))) {
            return "No";
        }

        return "Yes";
    }
}










































