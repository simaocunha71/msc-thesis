        int open_braces = 0;
        int close_braces = 0;

        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open_braces += 1;
                } else if (c == ')') {
                    close_braces += 1;
                }
            }
        }

        if (open_braces == close_braces) {
            return "Yes";
        } else {
            return "No";
        }
    }
}

