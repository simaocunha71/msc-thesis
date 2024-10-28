        int open_count = 0;
        int close_count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open_count += 1;
                if (c == ')') close_count += 1;
            }
        }
        if (open_count != close_count) return "No";
        return "Yes";
    }
}

