        int digits = 0;
        int index = file_name.indexOf('.');
        if (index < 0) {
            return "No";
        }
        for (char c : file_name.toCharArray()) {
            if (c >= '0' && c <= '9') {
                digits += 1;
                if (digits > 3) {
                    return "No";
                }
            }
        }
        String file_type = file_name.substring(index + 1).toLowerCase();
        if (file_type.equals("txt") || file_type.equals("exe") || file_type.equals("dll")) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

