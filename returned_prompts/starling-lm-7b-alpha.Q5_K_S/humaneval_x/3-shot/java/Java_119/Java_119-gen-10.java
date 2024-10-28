        int open = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open += 1;
                } else {
                    open -= 1;
                    if (open < 0) return "No";
                }
            }
        }
        return open == 0 ? "Yes" : "No";
    }
}

