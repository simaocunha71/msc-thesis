        int open_count = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open_count += 1;
                } else if (c == ')') {
                    open_count -= 1;
                }
                if (open_count < 0) return "No";
            }
        }
        return open_count == 0 ? "Yes" : "No";
    }
}

