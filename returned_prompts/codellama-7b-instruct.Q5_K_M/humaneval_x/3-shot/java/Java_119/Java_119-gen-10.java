        int open = 0;

        for (String s : lst) {
            for (char c : s.toCharArray()) {
                if (c == '(') {
                    open += 1;
                } else {
                    open -= 1;
                }
            }
        }
        return (open == 0) ? "Yes" : "No";
    }
}

