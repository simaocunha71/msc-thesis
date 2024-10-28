        int openCount = 0, closeCount = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    openCount++;
                } else if (c == ')') {
                    closeCount++;
                }
            }
        }
        return (openCount == closeCount) ? "Yes" : "No";
    }
}

