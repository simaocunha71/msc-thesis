        int depth = 0;
        for (String part : lst) {
            for (char c : part.toCharArray()) {
                if (c == '(') {
                    depth += 1;
                } else if (c == ')') {
                    depth -= 1;
                }
                if (depth < 0) {
                    return "No";
                }
            }
        }
        if (depth != 0) {
            return "No";
        }
        return "Yes";
    }
}

