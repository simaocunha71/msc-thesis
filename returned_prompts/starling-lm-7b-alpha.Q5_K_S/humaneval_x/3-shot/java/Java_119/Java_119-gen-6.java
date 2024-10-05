        int total_depth = 0;

        for (String string : lst) {
            for (char c : string.toCharArray()) {
                if (c == '(') {
                    total_depth += 1;
                } else if (c == ')') {
                    total_depth -= 1;
                }
                if (total_depth < 0) return "No";
            }
        }
        if (total_depth != 0) return "No";
        return "Yes";
    }
}

