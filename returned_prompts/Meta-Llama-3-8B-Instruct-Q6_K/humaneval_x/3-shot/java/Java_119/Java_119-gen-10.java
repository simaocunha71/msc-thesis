        int open_count = 0;
        int close_count = 0;

        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open_count++;
                } else if (c == ')') {
                    close_count++;
                }
            }
        }

        if (open_count == close_count) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

