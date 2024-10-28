        int depth = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') depth += 1;
                else depth -= 1;
                if (depth < 0) return "No";
            }
        }
        return (depth == 0) ? "Yes" : "No";
    }
}

