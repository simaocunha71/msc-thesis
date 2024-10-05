        int depth = 0;
        int left_parens = 0;
        int right_parens = 0;
        for (String s : lst) {
            if (s.equals("(")) {
                left_parens += 1;
                depth += 1;
            } else {
                right_parens += 1;
                depth -= 1;
            }
        }
        if (depth != 0) return "No";
        if (left_parens != right_parens) return "No";
        return "Yes";
    }
}

