        int num_of_digits = 0;
        int index_of_dot = file_name.indexOf('.');
        String before_dot = file_name.substring(0, index_of_dot);
        String after_dot = file_name.substring(index_of_dot + 1);

        for (char c : before_dot.toCharArray()) {
            if (c >= '0' && c <= '9') num_of_digits += 1;
        }

        if (num_of_digits > 3 || num_of_digits == 0 || index_of_dot == -1 || !Character.isLetter(before_dot.charAt(0)) || after_dot.length() == 0 || !after_dot.equals("txt") && !after_dot.equals("exe") && !after_dot.equals("dll")) {
            return "No";
        } else {
            return "Yes";
        }
    }
}

