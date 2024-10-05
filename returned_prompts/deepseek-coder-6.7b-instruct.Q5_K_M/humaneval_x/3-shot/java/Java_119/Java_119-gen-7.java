        int open = 0, closed = 0;
        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open++;
                } else if (c == ')') {
                    if (open > 0) {
                        open--;
                    } else {
                        closed++;
                    }
                }
            }
        }
        return (open == closed) ? "Yes" : "No";
     }
}

