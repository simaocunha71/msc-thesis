        int open_count = 0;
        int close_count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open_count += 1;
                } else if (c == ')') {
                    close_count += 1;
                }
            }
        }
        return open_count == close_count ? "Yes" : "No";
    }
}

