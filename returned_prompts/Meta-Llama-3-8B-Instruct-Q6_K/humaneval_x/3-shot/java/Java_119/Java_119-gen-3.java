        int open = 0, close = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') open++;
                if (c == ')') close++;
            }
        }
        return (open == close) ? "Yes" : "No";
    }
}

